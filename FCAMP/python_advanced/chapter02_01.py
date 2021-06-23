# 파이썬 데이터 모델링
# Namedtuple
# Namedtuple attrs
# Namedtuple method
# List Comprehension
# 구조화된 모델 설명


# Chapter 02-1
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조: http://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value
# 파이썬 -> 일관성

# 일반적인 튜플 사용

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print('Ex1-1 -', line_leng1)

# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Points', 'x y') # 맨 앞에는 뭘써줘도 상관은 없다, 클래스처럼 운영

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

print('Ex1-2 -', line_leng2)
print('Ex1-3 -', line_leng1 == line_leng2)

print()
print()

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y, z') # 이런식으로 방식을 합쳐서 써도 되긴하는데 가급적 정해서 한 스타일로 쓰자
Point4 = namedtuple('Point', 'x y x class', rename=True) # default = False


# Dict to Unpacking, 풀때 **을 달면 된다
temp_dict = {'x': 75, 'y': 55, 'z':20}

# 출력
print('Ex2-1 -', Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(5, y=20, z=10)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print('EX2-2 -', p1, p2, p3, p4, p5)

print()
print()

# 사용
print('EX3-1 -', p1[0] + p2[1]) # Index Error 주의
print('EX3-2 -', p1.x + p2.y) # 클래스 변수 접근 방식

# Unpacking, 아래처럼 변수명=값을 역으로 쓰면 언팩
x, y, z = p3 

print('EX3-3 -', x+y+z)

# Rename 테스트
print('EX3-4 -', p4)

print()
print()

# 네임트 튜플 메소드

temp = [52, 38]

# _make() : 새로운 객체 생성
p5 = Point1._make(temp)

print('EX4-1 -', p4)

# _fields: 필드 네임 확인
print('EX4-2 -', p1._fields, p4._fields)

# _asdict(): OrderedDict 반환

print('EX4-3 -', p1._asdict(), p4._asdict())

# _replace() : 수정된 '새로운' 객체 반환

print('EX4-4 -', p2._replace(y=100))

print()
print()


# 실 사용 실습
# 학생 전체 그룹 생성
# 반20명, 4개의 반 -> (A,B,C,D) 번호

# 네임트 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number']) # 맨 앞 튜플명은 관례상 변수명과 동일하게 설정

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)] # 해석: for 문을 돌려서 str(n)으로 저장, a for b in c = for every b in c, save it as a
ranks = 'A B C D'.split()

# List Comprehension(아래 처럼 표현하는게 리스트 컴프리헨션)
# 아래 구문 해석, 네임드 튜플의 rank, number에다가 for문 1번(A,B,C,D) 에 대해서 (1~20)을 각각 넣어라
# 즉, A에 대해서 1~20 을 하고, B, C, D를 반복해라
students = [Classes(rank, number) for rank in ranks for number in numbers] 

print('EX5-1 -', len(students)) # 80
print('EX5-1 -', students) # 80

# 너무 남발하면 가독성이 없다, 아래가 해석이 한번에 되겠냐? 
students2 = [Classes(rank, number) 
                for rank in 'A B C D'.split()
                    for number in [str(n) 
                        for n in range(1,21)]]

print()
print()

print('EX6-1 -', len(students2))
print('EX6-1 -', students2)

print()
print()

# 출력
for s in students:
    print('EX7-1 -', s)
