from icecream import ic

from context.domain import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemplate:
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()
        models = TitanicModel(train_fname='train.csv',test_fname='test.csv')
        ic(models)
