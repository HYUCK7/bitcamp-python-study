import random
import string

import numpy as np
import pandas as pd
from icecream import ic
from context.models import Model

from Algorithm.domains import myRandom


class Quiz30:
    def quiz30_df_4_by_3(self):
        # (1)
        a = []
        b = []
        c = []
        d = []
        col = [chr(i) for i in range(32, 35)]  # ['A','B','C']
        [a.append(i) if i < 4 else b.append(i) for i in range(1, 7)]
        [c.append(i) if i < 10 else d.append(i) for i in range(7, 13)]
        dict = {'1': a, '2': b, '3': c, '4': d}
        df = pd.DataFrame.from_dict(dict, orient='index', columns=col)
        ic(df)

        # (2)
        e = [[j * 3 + i for i in range(1, 4)] for j in range(4)]
        df1 = pd.DataFrame(e, index=range(1, 5), columns=col)
        ic(df1)
        # j = [1,2,3] * 3 + 1

        # 수업
        l1 = [range(1, 4)]
        l2 = [range(1, 4)]
        l3 = [range(1, 4)]
        l4 = [range(1, 4)]

    def quiz31_rand_2_by_3(self):
        c = [i for i in range(0, 3)]  # 0 , 1,  2
        # (1)
        # myRandom()
        # [a.append(myRandom(10,100)) for i in range(3)]
        # [b.append(myRandom(10,100)) for i in range(3)]

        # [a.append(myRandom(10, 100)) if i < 3 else b.append(myRandom(10, 100)) for i in range(6)]
        # dict = {'0': a, '1': b}
        # df = pd.DataFrame.from_dict(dict, orient='index', columns=c)
        # ic(df)

        # (2)
        e = [[myRandom(10, 100) for i in range(3)] for j in range(2)]
        df1 = pd.DataFrame(e, index=range(0, 2), columns=c)
        ic(df1)

    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    def quiz32_df_grade(self):
        data1 = np.random.randint(0, 100, (10, 4))
        col1 = ['국어', '영어', '수학', '사회']
        idx = [self.id(chr_size=5) for i in range(10)]
        df1 = pd.DataFrame(data1, index=idx, columns=col1)

        data2 = {i: j for i, j in zip(idx, data1)}
        df2 = pd.DataFrame.from_dict(data2, orient='index', columns=col1)

        ic(df1)
        ic(df2)

    def quiz33(self):
        d = [dict(zip(['a', 'b', 'c', 'd'],
                      np.random.randint(0, 100, 4))) for _ in range(3)]
        df = pd.DataFrame(d)

        df1 = self.createDF(keys=['a', 'b', 'c', 'd'],
                            vals=np.random.randint(0, 100, 4),
                            length=3)
        # print(df1)

        df2 = pd.DataFrame()

        # myGrade.csv
        '''subjects = ['java', 'py', 'js', 'sql']
        students = members()
        scores = np.random.randint(0, 100, (24,4))
        students_scores = pd.DataFrame(scores, index=students, columns=subjects)
        ic(students_scores)'''

        # df500.to_csv('./save/myGrade.csv', sep=',', na_rep='NaN')
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        # grade.csv
        model = Model()
        grade_df = model.new_model('grade.csv')
        df = pd.DataFrame(grade_df)
        print(df)

        # Q1. 파이썬 점수 출력
        python_scores = df.loc[:, ['파이썬']]
        ic(type(python_scores))
        ic(python_scores)
        # Q2. 조현국의 점수만 출력하시오
        cho_scores = df.loc['조현국']
        ic(type(cho_scores))
        ic(cho_scores)
        # Q3. 조현국의 과목별 점수를 출력하시오
        cho_scores1 = df.loc[['조현국']]
        ic(type(cho_scores1))
        ic(cho_scores1)
    @staticmethod
    def createDF(keys, vals, length):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(length)])

    def quiz34(self) -> str:
        '''
        df1.iloc[0]: a     0
                 b    54
                 c    74
                 d    63
                 Name: 0, dtype: int32

        ic(df1.iloc[[0]])

        ic| df1.iloc[[0]]:     a   b   c   d
                            0  86  64  13  46

        ic(df1.iloc[[0, 1]])

        ic| df1.iloc[[0, 1]]:   a   b  c   d
                             0  22  92  7  29
                             1  22  92  7  29

        ic(df1.iloc[:3])

                    a   b   c   d
                  0  24  74  88  27
                  1  24  74  88  27
                  2  24  74  88  27

        ic(df.iloc[[True, False, True]])

        ic| df.iloc[[True, False, True]]:      a   b   c   d
                                            0  14  77   5  43
                                            2  30  93  14  96

        ic(df.iloc[lambda x: x.index % 2 == 0])

        ic| df.iloc[lambda x: x.index % 2 ==0]:     a   b   c   d
                                        0  74  13  51  77
                                        2  25  91  74  49
        java -> , js => , py : (Lambda)

        ic(df.iloc[0, 1])
        ic| df.iloc[0,1]: 23

        ic(df.iloc[[0, 2], [1, 3]])

        ic| df.iloc[[0,2], [1,3]]:     b   d
                                    0  63  98
                                    2  62  31

        ic(df.iloc[1:3, 0:3])

        ic| df.iloc[1:3, 0:3]:     a   b   c
                       1  66  43   3
                       2  42   4  13

        ic(df.iloc[:, [True, False, True, False]])

        ic| df.iloc[:, [True,False,True,False]]:     a   c
                                         0  24  40
                                         1  54  61
                                         2  47  64

        ic(df.iloc[:, lambda df: [0, 2]])

        ic| df.iloc[:, lambda df:[0,2]]:     a   c
                                 0  59   0
                                 1  47  58
                                 2  16   7
        return None
        '''

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
