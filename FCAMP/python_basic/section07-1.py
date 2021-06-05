# 클래스 선언 및 self의 이해
# - 클래스 선언
# - 클래스 네임스페이스 Self
# - 클래스, 인스턴스 변수
# - Self

# Section 07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성됨
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제1, 첫글자는 대문자, 단어가 연결될떄도 대문자로, 속성과 메소드로 구성되며, 클래스 안에 pass 가 들어가면 에러는 안난다. 
class UserInfo:
    # 속성, 메소드
    def __init__(self, name1): # 클래스 초기화 용도 (== 생성자)
        self.name2 = name1
    def user_info_p(self):
        print('what: ', self.name2)

# 네임스페이스
user1 = UserInfo('Kim') # 클래스를 선언한 후 인스턴스화 해서 사용(붕어빵 기계로 붕어빵을 찍음, 인스턴스 생성 과정)
print(user1.name2)  # 속성 출력
user1.user_info_p() # 메소드

user2 = UserInfo('Park')
print(user2.name2)
user2.user_info_p()

print(id(user1)) # 메모리 주소값, 각각 다른 주소값을 가짐
print(id(user2))
print(user1.__dict__)  # namespace 출력, key와 value로 구성되며, self.name2 에서의 name2를 키값으로, name1은 value로 받음
print(user2.__dict__)


# 예제2
# self의 이해 
class SelfTest:
    def function1():  # 클래스 메소드, 그냥 클래스에 .달고 쓰면 됨. 반대로 인스턴스 생성한다고 쓸 수 있는건 아님
        print('function1 called!')
    def function2(self): # 인스턴스 메소드, self 인자에 인스턴스가 들어가면서 실행됨. 즉 인스턴스를 생성해야 쓸 수 있는 메소드임
        print('function2 called')

self_test = SelfTest()
# self_test.function1() : 실행이 안된다. 

SelfTest.function1() # 1. 클래스 메소드는 그냥 공통함수처럼 쓴다는 생각으로 클래스.함수로 지정
self_test.function2() # 2. 인스턴스 메소드는 인스턴스를 지정한 후에 인스턴스.함수로 지정하면 됨
SelfTest.function2(self_test) # 3. 인스턴스 메소드를 실행하기 위해 클래스.함수(인스턴스) 로 지정

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수, 클래스 안에서의 전역변수(공유 개념)
    stock_num = 0 
    def __init__(self, name): # 인스턴스 변수
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self): # 인스턴스 변수
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 3, 인스턴스 변수안에서 없으면 전역변수를 찾고 그것도 없으면 에러가 남
print(user2.stock_num) # 동일하게 3개
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)

