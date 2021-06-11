# 다양한 Exceptions
# - 파이썬 예외 종류
# - 문법적예러 발생 실습
# - 런타임 에러 발생 실습
# - Try-excep-else-finally

# Section 10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(린터임) 프로세스에서 발생하는 예외 처리도 중요
# linter: 코드 스타일, 문법 체크

# SyntaxError: 잘못된 문법

# ex1-1) 프린트문에 뒤에 '가 없다
# print('Test)

# ex1-2) if문인데 :가 안달려있다
# if True
#     pass 

# ex1-3) x->y 인데 => 인 정의되지 않은 기호를 썼다
# x => y


# NameError: 참조변수 없음
a = 10
b = 15

# ex2-1) 변수가 없음
# print(c)

# ex2-2) ZeroDivisionError: 0 나누기 에러
# print(10/0)

# ex2-3) IndexError: 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[0])
# print(x[3])


# KeyError: 주로 dict에서 발생
dic = {'name':'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby']) # 키가없다!
print(dic.get('hobby')) # 키값 찾을때는 안전빵인 .get 함수를 쓰다(없으면 none이 나옴)


# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month()) # 패키지에 없는 속성(함수) 임 


# ValueError: 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10) # remove할 10이 없다
# x.index(8) # 찾을 8이 없담


# FileNotFoundError
# f = open('test.txt', 'r')  # 읽어올 파일이 없다!


# TypeError
x = [1,2]
y = (1,2)
z = 'test'

# print(x + y)  # 다른 형간 합이 안됨
# print(x + z)
# print(x + list(y)) # 이런식으로 형변환해서 할수는 있음 


#### 
# 정리: 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외처리 코딩 권장(EAFP 코딩 스타일)


# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
# except: 에러명1, 에러가 나면 이걸 실행
# except: 에러명2
# else: 에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

# 예제1-1 : try문이 성공하면 try문과 else문이 연속적으로 실행됨
name = ['Kim', 'Lee', 'Park']

try: 
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found - ValueError Occured')
else:
    print('Ok! else')

print('-------------------------------------------')
print('-------------------------------------------')

# 예제1-2 : try문이 실패하면 except문만 실행됨, 값을 못찾는 에러면 valueerror로 except 문을 구체화 작성
name = ['Kim', 'Lee', 'Park']

try: 
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found - ValueError Occured')
else:
    print('Ok! else')

print('-------------------------------------------')
print('-------------------------------------------')

# 예제2 : 어떤 에러가 날지 모르면 그냥 except만 쓸것
name = ['Kim', 'Lee', 'Park']

try: 
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found - Occured')
else:
    print('Ok! else')

print('-------------------------------------------')
print('-------------------------------------------')

# 예제3 : finally는 try고 뭐고 항상 실행됨
name = ['Kim', 'Lee', 'Park']

try: 
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:  # except Exception이 전체를 의미함(안써도 됨)
    print('Not found - Occured')
else:
    print('Ok! else')
finally:
    print('Finally ok!')

print('-------------------------------------------')
print('-------------------------------------------')

# 예제4: 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally: 
    print('Finally ok!')

print('-------------------------------------------')
print('-------------------------------------------')

# 예제5: except 종류별로 추출하고 싶으면 순서에 유의(마지막에 default except를 넣을 것)
try: 
    z = 'Cho'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except ValueError as l: # 이런식으로 as를 넣어도 되고, 아님 그냥 쓰고 싶은 문구를 쓴다
    print(l)
except IndexError:
    print('Not found it! - IndexError!')
except Exception: # default
    print('Not found it! - Default Error!')
else: 
    print('Ok! else')
finally: 
    print('Finally OK!')

print('-------------------------------------------')
print('-------------------------------------------')

# 예제6: raise 키워드로 예외를 직접 발생시킬 수도 있다. (파이썬에 지정된 에러말고 커스터마이징)
try:
    a = '333'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError  # 아니라면 무조건 이 에러를 내게 한다음에
except ValueError:
    print('문제 발생')  # 이 문구를 출력하게 하면 파이썬 지정에러를 무시하고 내 맘대로 에러형태를 정할 수 있다.
except Exception as f:
    print(f)
else: 
    print('Ok!') 