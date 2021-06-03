# 조건문, 반복문 중간 점검 퀴즈
# - 총 10 문제
# - List Comprehension
# - Print 함수로 결과 출력


# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for v in q1:
    if v =='가을':
        print(q1[v])

# 아래가 조금 더 배운 기준으로 
for k, v in q1.items():
    if k =='가을':
        print(v)


print()
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q2.items():
    if v == '사과':
        print('사과가 포함되어 있음')
        break
else: 
    print('사과 없음')

print()
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

a = 77

if a >= 81:
    print('A학점')
elif a >= 61:
    print('B학점')
elif a >= 41:
    print('C학점')
elif a >= 21:
    print('D학점')
else:
    print('E학점')


print()
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a, b, c = 12, 6, 18
best = a

if b > a:
    best = b
if c > b:
    best = c
if a > c:
    best = a

print('best:', best)

print()
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'

if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')

print()
# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v =='정':
        continue
    else:
        print(v, end='')

print()

# 6번에서 리스트 컴프리헨션 활용하는 방법
q6 = [x for x in q3 if x != '정']   # include x (for x in q3, if x != 정)
print('6번 리스트 컴프리헨션:', q6)


print()
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for n in range(1,101):
    if n % 2 == 1:
        print(n, end=',')

print()
# 7번에서 리스트 컴프리헨션 활용하는 방법
q7 = [x for x in range(1,101) if x % 2 == 1]
print('7번 리스트 컴프리헨션:', q7)



print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for v in q4:
    if len(v)>=5:
        print(v, end=' ')




print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q5:
    if v.isupper():
        continue
    else:
        print(v, end=' ')
print()

# 아니면 islower로 한번에 풀수도 

for v in q5:
    if v.islower():
        print(v, end=' ')


print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q6:
    if v.isupper():
        print(v.lower())
    else:
        print(v.upper())


# 리스트 컴프리헨션
# 일반적인 방법
numbers = []
for n in range(1,101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션을 쓰면
numbers2 = [x for x in range(1,101)]  # include x (for x in range(1,101))
print(numbers2)

# 일반화
x = [x for x in range(1, 100) if 조건문]