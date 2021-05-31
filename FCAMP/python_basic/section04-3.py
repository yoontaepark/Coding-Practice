# 파이썬 자료구조(list, tuple)
# - 리스트 특징
# - 튜플 특징
# - 인덱싱
# - 슬라이싱
# - 삽입, 삭제, 함수 사용

# Section 04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+ d[1])
print(e[2][1]) #한단들어가서 그 안의 1번째 인덱스(순서로는 두번째) 출력
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산, 리스트끼리 합쳐지거나 곱해진다
print(c+d)
print(c*3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77 # c[0] 값이 갈아끼워진다
print(c)

c[1:2] = [100, 1000, 10000] # 범위로 지정하면, 인덱스 1과 2 사이에 복수의 값들을 넣어준다
print(c)
c[1] = ['a', 'b', 'c'] # 인덱스 1 자리에 리스트로 값들을 넣어준다
print(c)

del c[1] # 그 인덱스번호의 값이 삭제됨 
print(c)
del(c[-1])
print(c)
print()

# 리스트 합수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 맨뒤에다가 값 추가 
print(y)
y.sort() # 오름차순 정렬
print(y)
y.reverse() # 역순으로 뒤집기 
print(y)
y.insert(2,7) # 인덱스 2번자리에 삽입
print(y) 
y.remove(2) # 인덱스가 아니라 데이터 2 자체를 삭제, 중복일 경우 가장 앞에꺼만 지움
print(y)
y.pop() # LIFO, 가장 뒤에 놈을 뺀다
print(y)
ex = [88,77]
y.append(ex) # [] 형태면 []형태로 추가해줌
print(y)

fx = [66,55]
y.extend(fx) # extend는 그냥 리스트 안의 값으로만 다중 추가해줌 (물론 맨뒤로 감)
print(y)
print()

# 삭제: del: 인덱스번호를 찾아가서 삭제, remove: 해당 데이터를 삭제(인덱스 아님), pop: 가장 뒤에꺼 인덱스 값을 삭제


# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(d[2][1]) # b

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)
print()


# 튜플 함수

z = (5,2,1,3,4)
print(3 in z)
print(z.index(5)) # 찾고자하는 값의 index위치를 출력
print(z.count(5)) # 찾고자하는 값이 몇개 나오는지











