# 파이썬 Magic 메소드 설명
# - Magic 메소드란?
# - 매직 메소드 생성 예제
# - 매직 메소드 객체 사용
# - 매직 메소드 예제 출력
# - 기타 내용

# Chapter02-2
# 파이썬 심화
# Special Method(Magic Method)
# 참조1: https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2: https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 매직메소드 기초 설명

# 기본형

print(int)

# 모든 속성 및 메소드 출력

print(dir(int))
print()
print()

n=100

# 사용
print('EX1-1 -', n+200)
print('EX1-2 -', n.__add__(200))
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(), bool(n)) # 앞과 뒤가 같은 뜻임
print('EX1-5 -', n*100, n.__mul__(100)) # 앞과 뒤가 같은 뜻임

print()
print()


# 클래스 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height
    
    # 기본 메소드, 인스턴스(변수)만 찍었을 때 나오는 메소드
    def __str__(self):
        return 'Student Class Info: {}, {}'.format(self._name, self._height)

    # __ge__는 >= 에 해당하는 메소드임
    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    # __le__는 <= 에 해당하는 메소드임
    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    # __sub__는 (-) 에 해당하는 메소드임
    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._height - x._height

# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# 매직메소드 출력
print('EX2-1 -', s1 >= s2)
print('EX2-2 -', s1 <= s2)
print('EX2-3 -', s1 - s2)
print('EX2-4 -', s2 - s1)

print()
print()


# 클래스 예제2

# 벡터
class Vector(object):
    # *args는 튜플을 받아서 해체하겠다는 소리임
    def __init__(self, *args):
        '''Create a vector, example: v = Vector(1,2)''' # .__doc__ 으로 찍으면 나오는 주석
        
        # args이 비었다면 0,0 // 아니면 (x,y) 를 받아서, x,y로 해체해서 저장 
        if len(args) == 0:
            self._x, self._y = 0,0
        else:
            self._x, self._y = args

    # __str__ 과 유사한 기능을 하는 기본설정을 출력하는 메소드
    def __repr__(self):
        '''Returns the vector informations''' # .__doc__ 으로 찍으면 나오는 주석
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, other):
        '''Returns the vector sum of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        '''Returns the vector sum of self and other'''
        return Vector(self._x * other, self._y * other)


# Vector 인스턴스 생성
v1 = Vector(3,5)
v2 = Vector(15,20)
v3 = Vector(7,0)
v4 = Vector()

# 메직메소드 출력
print('EX3-1 -', Vector.__init__.__doc__)
print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-3 -', Vector.__add__.__doc__)
print('EX3-4 -', v1, v2, v3, v4)
print('EX3-5 -', v1 + v2)
print('EX3-6 -', v1 * 4)





    
    

        
