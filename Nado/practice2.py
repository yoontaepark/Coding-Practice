#Practice2
#연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2
print('\n')

print(2**3) # 2^3
print(5%3) # 나머지 구하기, 따라서 2가 나옴
print(5//3) # 몫 구하기, 따라서 1이 나옴
print('\n')

print(10 > 3) # True
print(4 >= 7) # False
print(5 <= 5) # True
print('\n')

print(3 == 3) # 왼쪽과 오른쪽이 같은지를 판정, True
print(4 == 2) # False
print(3 + 4 == 7) # True
print('\n')

print(1 != 3) # !=, 같지 않다는 뜻, True
print(not(1 != 3)) # not, 오른쪽 내용이 아니라는 뜻, 따라서 False
print((3 > 0) and (3 < 5)) #and 는 둘다 성립해야함, True
print((3 > 0) & (3 < 5)) # &로 표기해도 됨

print((3 > 0) or (3 > 5)) #or 는 하나만 성립하면 됨, True
print((3 > 0) | (3 > 5)) # |로 대체해서 써도 됨, |는 Shift+backspace 왼편 키

print(5 > 4 > 3) # 다중 등호 넣어도 됨, 이 경우 성립하니 True
print(5 > 4 > 7) # 이 경우 뒷편 4 > 7 이 틀렸으니 False

# 간단한 수식
print(2 + 3 * 4) # 생각하는데로 연산 우선순위가 잡힘, 14
print((2 + 3) * 4) # 생각하는데로 먼저 괄호안부터 계산, 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 변수가 상수라면, 왼편과 같이 연산 표현가능, 16
number += 2 # 위와 똑같으며 축약형임. 18
print(number)
number *= 2 # 곱셈도 왼편과 같이 표현가능, 36
print(number)
number /= 2 # 나눗셈도 동일, 18
print(number)
number -= 2 # 뺄셈도 동일함, 16
print(number)

number %= 5 # 나머지 구하기도 동일, 이 경우 1 
print(number)

# 숫자처리함수
print(abs(-5)) # 절대값 abs, 5
print(pow(4,2)) # 지수형 표현, 4^2
print(max(5,12)) # 큰 수를 출력함, 12
print(min(5,12)) # 작은 수를 출력함, 5
print(round(3.14)) # 반올림, 이 경우 정수형으로 출력함, 3

from math import *  # math 라이브러리의 전체(*) 를 사용하겠다는 뜻
print(floor(4.99)) # 내림, 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) # 제곱근, 4

# 랜덤함수
from random import * # random 라이브러리의 전체를 사용
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만
print(int(random() * 10 + 1)) # 1 ~ 10 이하(정확히는 11 미만인 정수)

# example: lottery
print(int(random() * 45 + 1)) # 방법1) 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 방법2) 1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) # 방법3) 1 ~ 45 이하의 임의의 값 생성(이게 좋아보임) 

'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오. 

조건1: 랜덤으로 날짤르 뽑아야 함
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외 

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. 
'''
# Answer
# from random import * 넣어놓기
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + " 일로 선정되었습니다.")

