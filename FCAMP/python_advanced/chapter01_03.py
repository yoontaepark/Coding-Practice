# Chapter 01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 메소드 상세 설명
# - 클래스 상세 설계
# - Class Method
# - Instance Method
# - Static Method
# - 효율적인 클래스 설계 설명

# 기본 인스턴스 메소드

class Student(object):
    '''
    Student Class
    Author: Park
    Date: 2021.05.26
    Description:
    '''

    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{},{}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Instance Method (기본정보 제공용 메소드)
    def __str__(self):
        return 'Student Info -> name: {}, grade: {}, email: {}'.format(self.full_name(), self._grade, self._email)


    # Class Method
    @classmethod
    def raise_fee(cls, per): # cls 자리에는 class 명을 넣어도 된다.
        if per <= 1:
            print('Please enter a number more than 1')
        cls.tuition_per = per
        print('Succed! tuituion has increased by {}'.format(cls.tuition_per))


    # Class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)


    # Static Method, 참고로 잘 안쓰는 추세가 되고 있음 
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient'



student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@daum.net', '2', 500, 4.3)

# __str__ 이 없었다면  걍 오브젝트가 출력됨 
# print(dir(student_1)) : 해당 인스턴스 변수에 적용되어 있는 모든 메소드들을 출력
# print()
# print(student_1.__dict__) : 해당 인스턴스가 가지고 있는 데이터가 뭐뭐 있는지 출력
print(student_1)
print(student_2)

print()

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보(인상전)
print(student_1.get_fee())
print(student_2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2

# 클래스 메소드 사용시 아래와 같이 cls 부분은 무시하고 뒤에 값만 넣어주면 된다. 
Student.raise_fee(1.5)

# 학비 정보(인상후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()

# 클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'Student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghan', 'Student4@gmail.com', '4', 600, 4.1)

# 전체 정보
print(student_3.detail_info())
print(student_4.detail_info())
print()

# 학생 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)
print()


# 장학금 혜택 여부(스테이틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()

# 장학금 혜택 여부(스테이틱 메소드 사용시)
# 클래스로도 메소드 호출할 수 있고, 
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()

# 인스턴스 변수로도 메소드 호출할 수 있음
print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))
