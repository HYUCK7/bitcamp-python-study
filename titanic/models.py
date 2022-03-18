from gc import garbage

import numpy as np
import pandas as pd
from icecream import ic

import context.models
from context import models, domain
from context.domain import Dataset
from context.models import Model


class TitanicModel:
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',
                   'Cabin', 'Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']  # 실제값
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Name')
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        # self.kwargs_sample(names='이순신')

        '''
        df = self.name_nominal(df)
        df = self.pclass_nominal(df)
        df = self.sex_nominal(df)
        df = self.embarked_nominal(df)
        df = self.age_ratio(df)
        df = self.fare_ratio(df)
        df = self.create_train(df)
        return df
        '''
        # self.print_this(this)
        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'9. id의 타입 {type(this.id)}')
        ic(f'10.id의 상위 10개 {this.id[:10]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
        """
        for i in feature:
        this.train = this.train.drop(i, axis=1)
        this.test = this.test.drop(i, axis=1)
        return this
        """
        [j.drop(i, axis=1, inplace=True) for i in feature for j in [this.train, this.test]]
        return this

    # 예제
    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))
        # tuple type
        # {print(''.join(f'key:{i},val:{j}')) for i, j in kwargs.items()}
        # key = name, value = '이순신'

    '''
    df = self.sibsp_garbage(df)
    df = self.parch_garbage(df)
    df = self.cabin_garbage(df)
    df = self.ticket_garbage(df)
    return df 가비지는 뤂으로 날려버림 메소드 만들 필요도 없다.
    '''

    '''
    categorical vs Quantitative
    cate -> nominal(이름) vs ordinal(순서)
    quan -> interval(상대적, 기준이 없음 ex)'부자',온도가 높다.낮다) vs ratio(절대적)
    '''

    @staticmethod
    def pclass_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> None:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        # this.train = this.train.drop('Sex', axis=1)
        # this.test = this.test.drop('Sex', axis=1)
        return this

    @staticmethod
    def extract_title_from_name(this) -> None:
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.',
                                                    expand=False)  # 정규식 신택스 안에서 [ ] , ?, + (반드시 있어얗나다.) 등 쓰이면 정규식
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        a = list(set(a))
        # print(f'>>> {a}')
        '''
        ['Lady', 'Mr', 'Dona', 'Mlle', 'Capt', 'Master', 'Jonkheer', 'Mrs', 'Countess',
        'Dr', 'Ms', 'Miss', 'Rev', 'Col', 'Sir', 'Major', 'Don', 'Mme','Mrs,'Master,'Capt]
        
        Royal : ['Countess', "Lady', 'Sir']
        Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme']
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        # title을 카테고리 컬로 줬음
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        # Null값을 -0.5로 바꿔서 -1과 0 사이에 두어 언노운을 만들어주기 위해서 -1과 0사이에 포함시키기 위해서

        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # labels를 지정해 줄 수 있으며, 지정한 bins의 개수보다 1 개가 적어야 합니다.
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior'] # (-1 ~ 0 unknown, 60 ~ Senior)
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['AgeGroup'] = pd.cut(these['Age'], bins, labels=labels, right=False)  # pd.cut() 을 사용
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map() 을 사용
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        train = this.train
        test = this.test
        this.test['Fare'] = this.test['Fare'].fillna(1)
        bins = [-1, 8, 15, 31, np.inf]
        labels = [0, 1, 2, 3]
        for these in train, test:
            these['FareBand'] = pd.cut(these['Fare'], bins, labels=labels)

        # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')

        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this
    # 사우스 햄튼에 사람(노동자)들이 가장 많이 탔기 때문에 정규분포에 따라서, 사우스 햄튼으로 채우겠다.
