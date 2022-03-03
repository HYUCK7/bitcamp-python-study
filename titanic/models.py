from titanic.domain import Dataset
import numpy as np # alias
import pandas as pd


class Model:
    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context+this.fname)