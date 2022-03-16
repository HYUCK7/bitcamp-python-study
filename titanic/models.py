from gc import garbage

from icecream import ic

import context.models
from context import models, domain
from context.domain import Dataset
from context.models import Model


class TitanicModel:
    model = Model()
    dataset = Dataset()

    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)

    def preprocess(self):
        df = self.train  # 대상이 되는 객체 생성
        ic(f'트레인 컬럼 {df.columns}')
        ic(f'트레인 헤드 {df.head()}')
        ic(df)

        df = self.drop_feature(df)
        df = self.name_nominal(df)
        df = self.pclass_nominal(df)
        df = self.sex_nominal(df)
        df = self.embarked_nominal(df)
        df = self.age_ratio(df)
        df = self.fare_ratio(df)
        df = self.create_label(df)
        df = self.create_train(df)
        return df

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def create_train(df) -> object:
        return df

    def drop_feature(self, df) -> object:
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
    def pclass_nominal(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df


    @staticmethod
    def fare_ratio(df) -> object:
        return df


    @staticmethod
    def embarked_nominal(df) -> object:
        return df
