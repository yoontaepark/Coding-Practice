# 파이썬 구성요소 기초 학습
# 1. 인코딩(입력, 출력)
# 2. 변수
# 3. 조건문
# 4. 함수, 클래스, 인스턴스(객체)
# 5. 정보출력

# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)  # utf-8 임
print(sys.stdout.encoding) # utf-8 임

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Goodboy'

# 조건문
if myName == 'Goodboy':
    print('Ok')

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

# 변수선언 및 출력(한글), 가능은 한데 실무에서는 영어로만
이름 = '좋은사람'
print(이름)

# 함수 선언
def 인사():
    print('안녕하세요. 반갑습니다.')

인사()

def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))