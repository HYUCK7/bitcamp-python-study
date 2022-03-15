from icecream import ic

import context.models
from context import models, domain
from context.domain import Dataset
from context.models import Model


class TitanicModel:
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)

    def preprocess(self):
        self.sibsp_garbage()
        self.parch_garbage()
        self.cabin_gabage()
        self.ticket_garvage()
        self.name_nominal()
        self.pclass_nominal()
        self.sex_nominal()
        self.embarked_nominal()
        self.age_ratio()
        self.fare_ratio()
        self.create_label()
        self.create_train()

    def create_label(self) -> object:
        pass

    def create_train(self) -> object:
        pass

    def drop_feature(self) -> object:
        pass

    '''
    categorical vs Quantitative
    cate -> nominal(이름) vs ordinal(순서)
    quan -> interval(상대적, 기준이 없음 ex)'부자',온도가 높다.낮다) vs ratio(절대적)
    '''

    def pclass_nominal(self) -> object:
        pass

    def sex_nominal(self) -> object:
        pass

    def name_nominal(self) -> object:
        pass

    def age_ratio(self) -> object:
        pass

    def sibsp_garbage(self) -> object:
        self.drop_feature()

    def parch_garbage(self) -> object:
        self.drop_feature()

    def fare_ratio(self) -> object:
        pass

    def cabin_gabage(self) -> object:
        pass

    def ticket_garvage(self) -> object:
        pass

    def embarked_nominal(self) -> object:
        self
