from gc import garbage

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
        # entity
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        # object
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']  # 실제값
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Cabin', 'Ticket')

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
        self.print_this(this)

    @staticmethod
    def print_this(this) -> None:
        ic(f'1. Train의 타입 {type(this.train)}\n')
        ic(f'2. Train의 컬럼 {this.train.columns}\n')
        ic(f'3. Train의 상위 1개 {this.train.head(1)}\n')
        ic(f'4. Train의 null 개수 {(this.train.isnull().sum())}\n')
        ic(f'5. Test의 타입 {type(this.test)}\n')
        ic(f'6. Test의 컬럼 {this.test.columns}\n')
        ic(f'7. Test의 상위 1개 {this.test.head(1)}\n')
        ic(f'8. Test의 null 개수 {this.test.isnull().sum()}\n')
        ic(f'9. id의 타입 {type(this.id)}\n')
        ic(f'10.id의 상위 10개 {this.id[:10]}\n')

    # 모델이 될 것이다. 데이터셋만 갖고 있었는데, 원데이터를 테스트 데이터로 분리한다. 디스에게 시험을 치루게 할 것이다. 아이디와 라벨을 뽑아낸 이유는 모델에게 시험을 치루게 할 문제가 될 것이다.
    # 문제를 낸다. -> 13번은 죽었는가, 실패했을 경우, 패널티를 주고, 개체들을 통해서 일반화 과정을 거친다. 원래 있던 csv를 가지고, 객체로 만들어낸다. 그러면서, 점점 정답의 범주를 컴퓨터가 줄인다.
    # 이것은 지도학습

    @staticmethod
    def create_train(df) -> object:
        return df

    @staticmethod
    def drop_feature(this, *feature) -> object:
        pass

        '''for i in feature:
        this.train = this.train.drop(i, axis=1)
        this.test = this.test.drop(i, axis=1)
        return this'''

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
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this
