# For, while
# - 파이썬 코딩의 핵심
# - 시퀀스 타입 반복
# - Continue, Break
# - For - else 구문
# - 자료구조 변환

# Section 05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문: for, while

v1 = 1
while v1 <11:
    print('v1 is:', v1)
    v1 += 1

print()

for v2 in range(10): # 시작점은 0 이고 끝-1까지
    print('v2 is:', v2)

print()

for v3 in range(1, 11): # 시작부터 끝-1까지
    print('v3 is:', v3)

# 1~100합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1~100:', sum1)
print('1~100:', sum(range(1,101)))      # 위에서 처럼 반복문으로 해도 되지만, sum의 기능을 써도 된다 
print('1~100:', sum(range(1, 101, 2)))  # 1부터 100까지의 합인데 2씩 올라가면서 sum
print()

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']

for v in names: # v 자리에 아무거나 넣어도 된다 
    print('You are:', v) # 리스트니까 반복이 가능해서 반복출력이 수행됨

word = 'dreams'

for s in word:
    print('word:', s)

print('\n\n')

# 딕셔너리 반복문
my_info = {
    'name': 'Kim',
    'age' : 33,
    'city': 'Seoul'
}

# 기본 값은 키
for key in my_info:
    print('my_info', key)

# 값
for key in my_info.values():
    print('my_info', key)

# 키
for key in my_info.keys():
    print('my_info', key)

# 키 and 값, 단일변수만 뽑으면 튜플형태로 나옴
for key in my_info.items():
    print('my_info', key)


print()
# 키 and 값, 두개를 같이 뽑으면 각각 문자열
for k, v in my_info.items():
    print('my_info', k, v)


# 대문자는 소문자로, 소문자는 대문자로 출력하기
name = 'KennRY'

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print('found: 33!')
        break # 조건이 맞으면 바로 for문을 빠져나감 
    else:
        print('not found: 33!')


# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행, break문으로 빠져나갔다면 else 수행안됨)
for num in numbers:
    if num == 33:
        print('found: 33!')
        break # 조건이 맞으면 바로 for문을 빠져나감 
    else:
        print('not found: 33!')
else:
    print('No data for 33....')


# continue

lt = ['1', 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue  # 조건이 맞으면 for문으로 바로 올라가버림(아래를 실행하지 않음)
    print('타입:', type(v))


# 자료구조 변환
name = 'Niceman'
print(reversed(name))
print(list(reversed(name)))
print(tuple((reversed(name))))