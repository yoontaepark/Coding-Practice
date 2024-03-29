# 파이썬 참조 심화
# - 파이썬 객체 참조 다양한 특징
# - copy
# - deep copy
# - 매개변수 전달 주의할 점

# chapter 05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

# print('EX1-1 -')
# print(__name__)

# id(객체 주소) vs __eq__ (==, 값) 은 다르다의 증명
x = {'name': 'kim', 'age':33, 'city':'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)

z = {'name': 'kim', 'age':33, 'city':'Seoul', 'class':10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z)        # 같은 객체인지를 확인
print('EX2-8 -', x is not z)
print('EX2-9 -', x == z)        # 같은 값인지를 확인 

# Con) 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성) 비교, ==(__eq__) 는 값 비교

print()
print()

# 튜플 불변형의 비교, 두개는 값은 같지만 주소는 다름(다른 객체임)
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

# Copy, Deepcopy(얕은 복사, 깉은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1       # 얕은 복사, 같은 객체임
tl3 = list(tl1) # 깊은 복사, 다른 객체로 복사가 됨

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)   # 다른 객체


# 추가 증명, 튜플에 값이 추가되면, 아예 객체가 새로 생성된 것으로 봐야함
# 리스트에 튜플을 넣으면 객체가 새로 할당되므로 데이터 낭비나 소실이 발생할 수도 있다. 
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()

print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플 재 할당(객체가 새로 생성됨)
print('EX4-10 -', tl3)
print(id(tl1[2]))


# Deep Copy

# 장바구니 
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)
    
    def put_prod(self, prod_name):
        self._products.append(prod_name)
    
    def del_prod(self, prod_name):
        self._products.remove(prod_name)
    

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)  # 얕은 복사
basket3 = copy.deepcopy(basket1) # 깊은 복사

print('EX5-1 -', id(basket1), id(basket2), id(basket3)) # 표면적인 객체는 달라보이나 (1, 2)
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products)) # 내부적인 속성값은 같음(1, 2)

print()

basket1.put_prod('Orange')
basket1.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products) # 1과 2의 속성값이 같아서, 값이 같이 바뀌어버림 (불상사) 
print('EX5-5 -', basket3._products)


# 함수 매개변수 전달 사용법

# 정수는 원래 정의한 변수(원본)가 바뀌지 않음
def mul(x, y):
    x += y
    return x

x = 10
y = 5

print('EX6-1 -', mul(x,y), x, y) # x,y 값(원본) 안바뀜
print()

a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a,b), a ,b) # 가변형 a(딕셔너리) -> 원본 데이터가 변경됨

c = (10, 100)
d = (5, 10)

print('EX6-3 -', mul(c,d), c ,d) # 불변형 c(튜플) -> 원본 데이터 변경 안됨
    

# 파이썬 불변형 예외 (복사말고 중복된 값을 새로운 변수로 선언할 경우)
# str, bytes, frozenset, Tuple: 사본 생성x -> 참조 반환(즉, 같은 객체로 인식함)

tt1 = (1,2,3,4,5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))  # 같은 객체
print('EX7-2 -', tt1 is tt3, id(tt1), id(tt3))  # 뭘해도 튜플이니 같은 객체 