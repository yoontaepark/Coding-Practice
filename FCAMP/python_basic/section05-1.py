# IF(조건문)
# - 조건문 기본 형식
# - 관계 연산자 실습(>, >=, <, <=, ==, !=)
# - 논리 연산자 실습(and, or, not)
# - 다중 조건문(if, elif, else)
# - 중첩 조건문
# 참 거짓 종류(True, False)
# 참 : '내용', [내용], (내용), {내용}, 1 <- 내용이 있거나 1 
# 거짓: '', [], (), {}, 0 <- 빈값이거나 0 


# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print('Yes')

# 예2
if False:
    print('No')
    
# 예3
if False:
    print('No')
else: 
    print('Yes2')


# 관계연산자
# >, >=, <, <=, ==, !=
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


# 참 거짓 종류(True, False)
# 참 : '내용', [내용], (내용), {내용}, 1 <- 내용이 있거나 1 
# 거짓: '', [], (), {}, 0 <- 빈값이거나 0 

city = ''
if city: # city가 빈값이므로 false다 
    print('>>>>True')
else:
    print('>>>>False')


# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and:', a>b and b>c) # 둘다맞아야 참
print('or:', a>b or c>b)   # 둘중 하나라도 맞으면 참
print('not:', not a>b)     # 반대로 결과값
print(not False)
print(not True)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용 
print('ex1:', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 70
score2 = 'A'

if score1 >= 90 and score2 =='A':
    print('합격하셨습니다.')
else:
    print('죄송합니다. 불합격입니다')


# 다중조건문
num = 90 
if num >= 90:
    print('num 등급 A', num)
elif num >= 80:
    print('num 등급 B', num)
elif num >= 70:
    print('num 등급 C', num)
else:
    print('꽝!')


# 중첩조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print('A지망 지원 가능')
    elif height >= 160:
        print('B지망 지원 가능')
    else: 
        print('지원 불가')
else: 
    print('20세 이상 지원 가능')
