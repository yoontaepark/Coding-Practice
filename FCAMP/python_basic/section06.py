# 함수 정의 및 람다(lambda) 사용
# - 함수 선언
# - 함수 다양한 사용
# - 다양한 반환 값
# - *args, **kwargs
# - 람다 함수

# Section 06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요, 사용하기전에 선언해야 됨

# 예제1: 리턴이 없음, 함수만 수행하고 끝 
def hello(world):
    print('Hello,', world)

hello('Python')
hello(7777)

# 예제2: 리턴이 있는 경우, 함수를 수행한 결과값을 원 코드로 돌려줌 
def hello_return(world):
    val = 'Hello ' + str(world)
    return val

hreturn = hello_return('Python!!!!!')
print(hreturn)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val1, val2, val3)

# 예제3-2, 다중리턴 중 데이터 타입 변환
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] # 리스트로 받고 싶으면 받을 때 자료형을 선언해주면 된다. 

lt = func_mul(100)
print(type(lt), lt)


# 예제4
# *args, **kwargs 
# args

def args_func(*args): # *args: 매개변수 개수 상관없이 출력을 다 받아줌, tuple 형태로 나옴
    for t in args:
        print(t)   

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

def args_func2(*args):
    for i,v in enumerate(args): # enumarate는 인덱스와 값을 같이 출력
        print(i,v)   

args_func2('Kim')
args_func2('Kim', 'Park')
args_func2('Kim', 'Park', 'Lee')

# kwargs
def kwargs_func(**kwargs): # **kwargs: 매개변수 개수 상관없이 출력 다 받아줌, dict 형태로 나옴
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1='kim') # 매개변수 넣을때 컬럼명에 '' 안넣고 그냥 씀 
kwargs_func(name1='kim', name2='Park', name3='Lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=23)


# 예제5, 중첩함수(클로저), 함수 중첩해서 쓸 경우 코드 flow가 아래줄 코드부터 올라올 수도 있다. 
# 함수끼리 매개변수로 이어야하니, 매개변수명은 같게 설정해야 함

def nested_func(num):           # 2번
    def func_in_func(num):      # 5번
        print(num)              # 6번
    print('in func')            # 3번
    func_in_func(num + 10000)   # 4번
nested_func(100)                # 1번


# 예제6, 함수에 hint 주기, 매개변수가 어떤 자료형이 오고, 리턴값은 어떤 자료형이 된다를 힌트로 알려줌
# 물론 다른 자료형이 들어갈수도 있음(ex. int 대신 float이 들어간다고 에러가 나지는 않음)
def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] 

print(func_mul3(10))

# 람다식 예제
# 람다식: 메모리 절약, 가독성 향상(이건 케바케), 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10

print(type(mul_10), mul_10) # 함수자체가 사용이 안되더라도 메모리가 할당되어 있음

val_func = mul_10     
print(val_func)
print(type(val_func))
print(val_func(10))   

# 이때 lambda를 쓰면 메모리 할당하면서 바로 실행
lambda_mul_10 = lambda num: num*10  # num*10을 해서 왼편 num에 넣겠다는 소리
print('>>>', lambda_mul_10(10))

def func_final(x, y, z):
    print(x * y * z(10))

func_final(10, 10, lambda_mul_10) # 10 * 10 * 100 이 된다. 

print(func_final(10, 10, lambda x: x * 1000)) # 10 * 10 * 10000 이 된다. 