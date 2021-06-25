# Chapter 03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형이 들어갈 수 있음 [list, tuple, collections.deque]
# Flat: 한 개의 자료형만 들어갈 수 있음 [str, bytes, bytearray, array.array, memoryview]
# 가변: list, bytearray, array.array, memoryview, deque
# 불변: tuple, str, bytes


# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '!@#$$%^^&%$'
codes1 = []

for s in chars:
    codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars] # 위랑 똑같은 결과가 나오는데 한줄로 표현 가능하다

# Comprehending Lists + Map, Filter
# 속도가 약간 우세하다
codes3 = [ord(s) for s in chars if ord(s) > 40] # if문도 바로 추가할 수 있다
codes4 = list(map(ord, chars)) # map 함수가 이제 (a,b) 면 b를 a로 변환해달라라는 소리 

# if구문 처럼 쓸게 있다면 filter 함수를 사용하면 된다, 원데이터가 뒤로가고, 앞에는 조건을 넣으면 됨
codes5 = list(filter(lambda x : x > 40, map(ord, chars))) 


print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', codes5)

