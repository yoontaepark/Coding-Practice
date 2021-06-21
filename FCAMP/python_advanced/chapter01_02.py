# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수 

# 클래스 재 선언
class Student():

    """
    Student Class
    Author: YoontaePark
    Date: 2021.05.25
    """

    # 클래스 변수
    student_count = 0


    def __init__(self, name, number, grade, details, email=None):
        # 아래가 인스턴스 변수 
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1 # 이거도 클래스 변수

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id: {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1




# Self 의미, 클래스(붕어빵틀)로 인스턴스 변수(붕어빵)를 선언 
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 95, 'score2': 88})
studt2 = Student('Cho', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 44}, 'stu2@naver.com')

# ID 확인, 각기 다른 주소에 생성되었음을 알 수 있다. 
print(id(studt1))
print(id(studt2))

print(studt1._name == studt2._name) #value는 같으니까 True
print(studt1 is studt2) # 첫 인스턴스말고는 다 다르니까 False

# dir(세부속성, 다 나옴) & __dict__(기본속성, 값도 같이 알려줌, 이걸로 먼저 확인해보기) 확인
print(dir(studt1))
print(dir(studt2))
print(studt1.__dict__)
print(studt2.__dict__)

# Doctring (클래스의 주석 출력, 주석도 class 선언후 바로 아래에 달아야 출력이 됨 )
print(Student.__doc__)
print()

# 실행, 인스턴스 변수.메소드
studt1.detail_info()
studt2.detail_info()

# 에러
# Student.detail.info()
# 클래스.메소드()는 에러, 클래스.메소드(인스턴스 변수)는 가능

Student.detail_info(studt1)
Student.detail_info(studt2)

# 비교
print(studt1.__class__, studt2.__class__)  # 인스턴스 변수의 틀을 확인
print(id(studt1.__class__), id(studt2.__class__)) # 붕어빵 틀 의 주소는? 같다 

print()

# 인스턴스 변수
# 직접 접근 권장x (PEP 문법적으로 권장x)

# studt1._name = 'hhhh' , 이런거 하지말라는 소리
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

print()
print()

# 클래스 변수 

# 접근, 클래스변수는 클래스/인스턴스 모두가 공용으로 접근 가능
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인, 인스턴스 변수에는 student_count가 없지만 상위 클래스에 있으면 공유가 되므로 접근이 가능
print(Student.__dict__)
print(studt1.__dict__)
print(studt2.__dict__) 

# 인스턴스 네임스페이스에 없으면 상위에서 검색한다
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del studt2

print(studt1.student_count)
print(Student.student_count)
