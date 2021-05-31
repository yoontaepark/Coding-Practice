# 파이썬 자료구조(Dictionary, Set)
# - 딕셔너리 특징
# - 딕셔너리 추가
# - 집합 특징
# - 집합 자료형 함수
# - 자료형 변환

# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value(Json) -> MongoDB
# 선언
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1,2,3,4,5]}

print(type(a), type(b), type(c))

# 출력
print(a['name']) # 없는 키를 넣으면 에러가 남 
print(a.get('name')) # 없는 키를 넣더라도 none으로 출력
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (1,2,3)
print(a)


# keys, values, items(전체, 즉 key+value)
print(a.keys()) # 리스트 형태로 출력되지만, 아직 리스트는 아니다
print(list(a.keys())) # 따라서 리스트 형태로 반환한다음에 인덱싱이나 슬라이싱을 한다 

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(2 in b) # 이거는 키값을 가지고 판별함
print('arr' in c)
print('name2' not in a)


# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c) # 6은 중복허용 안하기 때문에 1,4,5,6 이렇게만 출력됨

t = tuple(b) # 형변환하면 변환한 형의 특성을 사용한다
print(t)
l = list(b)
print(l)

print('\n\n')

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection((s2))) # 교집합
print(s1 & s2)

print(s1 | s2)              # 합잡합
print(s1.union((s2)))

print(s1- s2)               # 차집합
print(s1.difference((s2)))

# 집합 - 추가&제거
s3 = set([7,8,10,15])

s3.add(18) 
s3.add(7) # 중복이 있다면 중복허용x 이므로 추가가 안됨
print(s3)

s3.remove(15)
print(s3)

print(type(s3))