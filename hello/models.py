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
    def __init__(self):
        pass
if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1. 계산기 (+, - , *, /) 2. BMI 계산기 3. 성적표')
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
