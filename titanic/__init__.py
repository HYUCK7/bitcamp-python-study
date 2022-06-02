# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic import models
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplate
from titanic.views import TitanicView


if __name__ == '__main__':
    # view = TitanicView()
    # models = TitanicModel(train_fname='train.csv', test_fname='test.csv')
    while 1:
        menu = (input('1.템플릿 2. 전처리'))
        if menu == '1':
            print(' #### 템플릿 ####')
            # models.TitanicModel(train='train.csv', test='test.csv')
            template = TitanicTemplate(fname='train.csv')
            template.visualize()
            break
        elif menu == '2':
            print(' #### 전처리 ####')
            model = TitanicModel()
            model.learning(train_fname='train.csv', test_fname='test.csv')
            break


