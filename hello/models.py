
import random
def main():
    while 1:
        menu = input('0.Exit 1. 계산기 (+, - , *, /) 2. BMI 계산기 3. 성적표 4. 오토성적표 5. 다이스 6. 추출 7. 멤버뽑기')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            calc = Quiz01Calculator(int(input('첫 번째 수')),int(input('두 번째 수')),input('연산기호'))
            print(f'{calc.num1} {calc.opcode} {calc.num2} = {calc.opcodeSelect()}')
        elif menu == '2': # BMI
            bmi = Quiz02Bmi(input('이름'), int(input('몸무게')), int(input('키')))
            print(f'{bmi.name}님의 결과는 {bmi.op()}')
        elif menu == '3': #Grade
            grade = Quiz03Grade(input('이름'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            print (f'''\
            {grade.name} 님의 성적표
            국어 점수 : {grade.kor}
            영어 점수 : {grade.eng}
            수학 점수 : {grade.math}
            총점 : {grade.total()}
            평균 : {grade.avg()}
            ''')
        elif menu =='4': #Gradeauto
            for i in ['김유신', '강감찬', '유관순', '윤봉길','신사임당']:
                print()
                pass
        elif menu == '5': #Dice
            print(Quiz05Dice.cast())

        elif menu == '6': pass

        elif menu == '7': # RandomChoice
            print(Quiz07RandomChoice().choice())
        elif menu == '8': #RPS
            q8 = Quiz08Rps(1)
            print(q8.game())
        elif menu == '9': #GetPrime
            primeValue = Quiz09GetPrime(int(input('숫자 값 입력')))
            print(primeValue.getP())
        elif menu == '10': #LeapYear
            pass
        elif menu == '11': #NumberGolf
            user = Quiz11NumberGolf(int(input('숫자 값 입력')))
            print(user.golf())

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
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def op(self):
        res = (self.weight / (self.height**2))*1000
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
        self.computer = myRandom(0,2)
        self.rps = ['가위', '바위', '보']
    def game(self):
        # 1 가위 2 바위 3보
        pass

        '''if p == 1:
            if c == 0: res = f'플레이어{rps[0]}, 컴퓨터{rps[0]}, 결과 draw'
            elif c == 1: res = f'플레이어{rps[0]}, 컴퓨터{rps[1]}, 결과 lose'
            elif c == 2: res = f'플레이어{rps[0]}, 컴퓨터{rps[2]}, 결과 win'
            
        if p == 2:
            if c == 1: res = 'lose'
            elif c == 2: res = 'draw'
            elif c == 3: res = 'win'
        if p == 3:
            if c == 1: res = 'lose'
            elif c == 2: res = 'win'
            elif c == 3: res = 'draw'''
        pass

class Quiz09GetPrime:
    def __init__(self, prime):
        self.prime = prime
    def getP(self):
        res = ''
        for i in range(2, self.prime):
            count = 0
            for j in range(2, self.prime +1):
                if i == j: res += str(i)
                elif i % j ==0: break
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
        res =""
        while self.user != self.com :
            if self.user > self.com: res = "Down"
            elif self.user < self.com: res = "Up"
            elif self.user == self.com: res = "정답."
            return res


class Quiz12Lotto:
    def __init__(self):
        pass
class Quiz13Bank:#이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan:#책받침 구구단
    def __init__(self):
        pass

if __name__ == '__main__':
    main()