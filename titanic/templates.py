from icecream import ic
from matplotlib import rc, font_manager

from context.domain import Dataset
from context.models import Model
from titanic import TitanicModel
import matplotlib.pyplot as plt
import seaborn as sns

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())

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
        f, ax = plt.subplots(1, 2, figsize=(18, 8))  # f = 형태 fig nrows=1, ncols=2, figsize=18inch, 8inch
        df['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0. 사망자 vs 1. 생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0. 사망자 vs 1. 생존자')
        sns.countplot('Survived', data=df, ax=ax[1])
        # plt.show()
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_survived.png')

    @staticmethod
    def draw_pclass(df) -> None:
        df['생존결과'] = df['Survived'] \
            .replace(0, '사망자').replace(1, '생존자')
        df['Pclass'] = df['Pclass'].replace(1, '1등석').replace(2, '2등석').replace(3, '3등석')
        sns.countplot(data=df)
        model = Model()
        plt.savefig(f'{model.get_sname()} draw_pclass.png')

    @staticmethod
    def draw_sex(df) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        df['Survived'][df['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0],
                                                                    shadow=True)
        df['Survived'][df['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1],
                                                                      shadow=True)
        ax[0].set_title('남성의 생존비율 [0.사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0.사망자 vs 1.생존자]')
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_sex.png')

    @staticmethod
    def draw_embarked(df) -> None:
        df['생존결과'] = df['Survived'] \
            .replace(0, '사망자').replace(1, '생존자')
        df['승선항구'] = df['Embarked'] \
            .replace("C", '쉘버그').replace("S", '사우스햄톤').replace("Q", '퀸즈타운')
        sns.countplot(data=df)
        model = Model()
        plt.savefig(f'{model.get_sname()}draw_embarked.png')
