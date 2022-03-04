
import random

class Quiz01Calculator(object):
    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def opcodeSelect(self):
        if self.opcode == "+" : return self.add()
        elif self.opcode == '-' : return self.sub()
        elif self.opcode == '*' : return self.mul()
        elif self.opcode == '/' : return self.div()

class Quiz02Bmi(object):
    @staticmethod
    def op(member):
        this = member
        res = (this.weight / (this.height**2))*1000
        if res < 18.5:
            return '저체중입니다.'
        elif res < 23:
            return '정상입니다.'
        elif res < 25:
            return '과체중입니다.'
        elif res < 30:
            return '비만입니다.'
        elif res > 30:
            return '고도비만입니다.'

class Quiz03Grade(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def total(self): return self.kor + self.eng + self.math
    def avg(self): return (Quiz03Grade.total(self))/3

class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def total(self): return self.kor + self.eng + self.math
    def avg(self): return (self.total())/3
    def getGrade(self):pass
    def chkPass(self): # 60점 이상이면 합격
        pass

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice:
    @staticmethod
    def cast(): return myRandom(1, 6)

class Quiz06RandomGenerator:
    def __init__(self): pass

class Quiz07RandomChoice:
    def __init__(self): #803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    # def choice(self): return self.members[int(random.random() * 24)]
    def choice(self): return self.members[myRandom(0,23)]

class Quiz08Rps:
    def __init__(self, player):
        self.player = player
        self.computer = myRandom(1,3)
        self.rps = ['가위', '바위', '보']
    def game(self): # 1 : 가위 2: 바위 3 :보
        res = ''
        if self.player - self.computer == -2 or self.player - self.computer == 1: res = 'win'
        elif self.player - self.computer == -1 or self.player - self.computer == 2: res = 'lose'
        elif self.player == self.computer: res = 'draw'
        return res

class Quiz09GetPrime:
    def __init__(self, prime):
        self.prime = prime
    def getP(self):
        res = ''
        for i in range(2, self.prime):
            count = 0
            for j in range(2, self.prime +1):
                if i % j ==0: count += 1
                if count == 1: res += str(i) + "\t"
                return res

class Quiz10LeapYear:
    def __init__(self,year):
        self.year = year
    def leap(self):
        if self.year % 4 == 0 and not self.year%100 == 0 or self.year%400==0: return '윤년'
        else: return '평년'

class Quiz11NumberGolf:
    def __init__(self, user):
        self.com = myRandom(1,100)
        self.user = user
    def golf(self):
        while self.user != self.com :
            if self.user > self.com: self.user = int(input('down'))
            elif self.user < self.com: self.user = int(input('up'))
        return '정답입니다.'


class Quiz12Lotto:
    @staticmethod
    def lotto():
        lottoNum = myRandom(1,46)
        check = []
        for i in range (6):
            i = lottoNum
        return sorted(check)
        pass
class Quiz13Bank:#이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan:#책받침 구구단
    @staticmethod
    def gugudan():
        res =""
        for k in [2,6]:
            for j in range(1,10):
                for i in range(0,4):
                    res += f'{i + k} * {j} = {(i+k) * j}\t'
                res += '\n'
            res += '\n'
        return res