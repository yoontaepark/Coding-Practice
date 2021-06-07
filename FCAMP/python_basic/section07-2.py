# 클래스 상속, 다중 상속
# - 클래스 상속
# - 클래스 상속 예제 코딩
# - 클래스 다중 상속

# Section 07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능(코드 재사용 가능, 효율적인 코딩 가능)

# 라면 -> 속성(종류, 회사,, 맛, 면 종류, 이름) : 부모

class Car:
    '''Parent Class''' # 주석처리 
    def __init__(self, tp, color):
        self.type = tp          # 부모 속성 (self.type을 말하는 것임!)
        self.color = color      # 부모 속성
    
    def show(self):  # 부모 메소드(자식이 다 쓸 수 있음)
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    '''Sub Class'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모 속성을 상속받음
        self.car_name = car_name    # 자식고유 속성 추가
    
    def show_model(self) -> None: # 자식 고유 메소드 (-> None은 힌팅)
        return 'Your Car Name : %s' % self.car_name 

class BenzCar(Car):
    '''Sub Class'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None: # -> None은 힌팅하는건데 안넣어도 됨
        return 'Your Car Name : %s' % self.car_name
    
    def show(self):     # 부모에 있는 메소드여도 덮어쓰기 할수 있음. 이 경우 이 메소드가 우선함
        print(super().show()) # 부모꺼 메소드를 쓰고 싶으면 자식 메소드에서 추가해서 선언, super(). 으로 선언하면 됨
        return 'Car Info: %s %s %s' % (self.car_name, self.type, self.color)


# 자식 클래스는 부모 클래스 전부 사용가능 + 자식 고유 속성/메소드 사용가능
# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red') # car_name, tp, color 

print(model1.type)          # Super
print(model1.color)         # Super
print(model1.car_name)      # Sub
print(model1.show())        # Super
print(model1.show_model())  # Sub
print(model1.__dict__)      

# Method Overriding(오버라이딩)
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

# Parent Method Call: 자식 매소드에다가 super. 으로 추가해두면 된다. 
model3 = BenzCar('3500d', 'sedan2', 'silver')
print(model3.show())

# Inheritance Info (상속정보 파악, .mro() 로 파악)
print(BmwCar.mro()) # 왼->오른으로 car상속, 최상위는 object임
print(BenzCar.mro())


# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class C(B, A, Z):
    pass

print(C.mro()) # B, A, Z, (Y,Z)-> Y, (X,Y) -> X 다 상속받고, 최상위 오브젝트로 끝남. 최상위 빼고는 그냥 다중 상속인거지 상속받는 클래스간 우열은 없음
print(A.mro()) # X, Y 상속, 최상위 오브젝트로 끝남

