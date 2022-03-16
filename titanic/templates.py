from icecream import ic

from context.domain import Dataset
from context.models import Model
from titanic import TitanicModel
import matplotlib.pyplot as plt

'''데이터 시각화
엔티티 (개체)를 차트로 표현하는 것.

survived, pclass, sex, embarked의 feature 작성. 템블릿 메소드 패턴으로 구성
init은 건들지 않는다.'''


class TitanicTemplate:
    model = Model()
    dataset = Dataset()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        df = self.entity
        ic(f'트레인의 타입: {type(df)}')
        ic(f'트레인의 컬럼: {df.columns}')
        ic(f'트레인의 상위 5행: {df.head()}')
        ic(f'트레인의 하위 5행: {df.tail()}')

    def visualize(self) -> None:
        df = self.entity
        self.draw_pclass(df)
        self.draw_sex(df)
        self.draw_embarked(df)
        self.draw_survived(df)

    @staticmethod
    def draw_survived(df) -> None:
        # f, ax = plt.subplots(1, 2, figsize=(18, 8))
        # this = ['Survived']
        plt.show()

    @staticmethod
    def draw_pclass(df) -> None:
        plt.show()

    @staticmethod
    def draw_sex(df) -> None:
        plt.show()

    @staticmethod
    def draw_embarked(df) -> None:
        plt.show()
