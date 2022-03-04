from Algorithm.domains import members
from hello import Member
from hello.domains import my100, myRandom


class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        op = o[myRandom(0,4)]

        if op == '+': res = self.add(a,b)
        elif op == '-': res = (self.sub(a,b))
        elif op == '*': res = (self.mul(a,b))
        elif op == '/': res = (self.div(a,b))
        elif op == '%': res = (self.mod(a,b))
        print(f'{a} {op} {b} = {res}')
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 86.8
        res = this.weight / (this.height * this.height) * 10000
        if res < 18.5:
            state = '저체중입니다.'
        elif res < 23:
            state = '정상입니다.'
        elif res < 25:
            state = '과체중입니다.'
        elif res < 30:
            state = '비만입니다.'
        elif res > 30:
            state = '고도비만입니다.'
        print(state)

    def quiz02dice(self):
        print( myRandom(1, 6) )

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'
        print(res)
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)
        print( ' ----------- 3 --------------')

    def quiz04leap(self):
            year = myRandom(1900,2050)
            if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
                res = '윤년'
            else:
                res = '평년'
            print(res)

    def quiz05grade(self):
        kor = myRandom(0,100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        grade = self.getGrade()
        passChk = self.passChk()
        print [sum, avg, grade, passChk]

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def grade(self):
        if self.avg() >90 : gra = 'A등급입니다.'
        elif self.avg() >75 : gra = 'B등급입니다.'
        elif self.avg() >60 : gra = 'C등급입니다.'
        elif self.avg() >40 : gra = 'D등급입니다.'
        else: gra = 'F등급입니다.'
        return gra

    def passChk(self):  # 60점이상이면 합격
        if self.avg > 70: pCheck = '합격'
        else: pCheck = '불합격'
        return pCheck

    def quiz06memberChoice(self):
        print(members[myRandom(0, 23)])

    def quiz07lotto(self):
        print (myRandom(range(0,46)))

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        guests = ['김김김', '임임임', '유유유']
        select = guests[range(0,2)]
        money = range(0,1000000)
        if select == '김김김': pass

    def quiz09gugudan(self):  # 책받침구구단
        res = ""
        for k in [2, 6]:
            for j in range(1, 10):
                for i in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        print(res)