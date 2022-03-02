import opcode
import random
def main():
    while 1:
        menu = input('0.Exit 1. 계산기 (+, - , *, /) 2. BMI 계산기 3. 성적표 4. 오토성적표 5. 다이스 6. 추출 7. 멤버뽑기')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            calc = Quiz01Calculator(num1, num2)
            num1 = int(input('첫 번째 수'))
            num2 = int(input('두 번째 수'))
            opcode = input('연산기호')
            print(f'{calc.num1} {opcode} {calc.num2} = {calc.opcodeSelect()}')
        elif menu == '2': # BMI
            bmi = Quiz02Bmi(name, height, weight)
            name = input('이름')
            weight = int(input('몸무게'))
            height = int(input('키'))
            print(f'{name}님의 결과는 {bmi.op()}')
        elif menu == '3': #Grade
            grade = Quiz03Grade(name, kor, eng, math)
            name = input('이름')
            kor = int(input('국어 점수'))
            math = int(input('수학 점수'))
            eng = int(input('영어 점수'))
            print (f'''\
            {name} 님의 성적표
            국어 점수 : {kor}
            영어 점수 : {eng}
            수학 점수 : {math}
            총점 : {grade.total()}
            평균 : {grade.avg()}
            ''')
        elif menu =='4': #Gradeauto
            for i in ['김유신', '강감찬', '유관순', '윤봉길','신사임당']:
                print()
                pass
        elif menu == '5': #Dice
            dice = Quiz05Dice(None)
            dic = dice.number()
            print(dic)

        elif menu == '6': # RandomGenerator
            randonNum = Quiz06RandomGenerator(int(input('범위 설정')))
            print(randonNum.number())

        elif menu == '7': # RandomChoice
            print(Quiz07RandomChoice().choice())

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
        if opcode == "+" : return self.add()
        elif opcode == '-' : return self.sub()
        elif opcode == '*' : return self.mul()
        elif opcode == '/' : return self.div()

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

class Quiz05Dice:
    def __init__(self,dic):
        self.dic = dic
    def number(self): return int(random.random() * 6) +1

class Quiz06RandomGenerator:
    def __init__(self,scope): #원하는 범위의 정수에서 랜덤값 1개 추출
        self.scope = scope
    def number(self): return int(random.random() * self.scope) + 1

class Quiz07RandomChoice:
    def __init__(self): #803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    def choice(self): return self.members[int(random.random() * 24)]
if __name__ == '__main__':
    main()