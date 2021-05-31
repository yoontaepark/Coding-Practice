# 문자형 관련 연산자
# - 문자열 생성, 길이
# - 이스케이프 문자
# - 문자열 연산
# - 문자열 형 변환
# - 문자열 함수
# - 문자열 슬라이싱

# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = 'I am Boy.'
str2 = 'NiceMan'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

# escape
escape_str1 = 'Do you have a \"big collection?\"'
print(escape_str1)
escape_str2 = 'Tab\ttat\ttab'
print(escape_str2)

# Raw String: r치고 뒤에 ''를 작성하면 ''안에 있는 내용이 그대로 출력됨
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r'\\a\\a'
print(raw_s2)

# 멀티라인, 변수 선언 다음에 \(escape) 를 치면 그다음에 이어지는구나 라고 생각하면 된다. 
multi = \
'''
문자열
멀티라인
테스트
'''

print(multi)

# 문자열 연산
str_01 = '*'
str_02 = 'abc '
str_03 = 'def'
str_04 = 'Niceman'

print(str_01 * 100)
print(str_02 + str_03)
print(str_01 * 3)
# a in b 의 경우 문자열 b에 문자 a가 있냐를 확인 후 bool 형으로 값을 리턴해줌
print('a' in str_04)
print('f' in str_04)
print('z' not in str_04)

# 문자열 형 변환, 설령 정수형이어도 문자열 형태로 변환해서 출력할 수 있다. (겉 껍데기는 숫자지만 type은 문자열)
print(str(77) + 'a')
print(str(10.4))


# 문자열 함수, 좋은게 많고 예시로 몇개만 해봄
# 참고: https://www.w3schools.com/python/python_ref_string.asp


# ctrl+/ 누르면 구간 주석처리가 됨
# a = 'niceman'
# b = 'orange'

# print(a.islower()) # 전부 소문자인지 확인해서 boolean 값을 리턴해줌
# print(b.endswith('e')) # 끝자리가 (문자) 로 끝나는지 확인
# print(a.capitalize()) # 첫글자만 대문자로 바꿔줌 
# print(a.replace('nice', 'good')) # 앞의 문자열을 뒤의 문자열로 바꿔줌
# print(list(reversed(b))) # 역순으로 바꾼 후 리스트로 출력


a = 'niceman'
b = 'orange'

print(a[0:3]) # index 0번부터 3번 미만(2번까지)
print(a[0:len(a)]) #index 처음부터 끝까지, len은 0번 제외하고 개수를 세기때문에 인덱스 처음부터 끝까지 셀때 이런식으로 쓸 것
print(a[:]) # index 전체
print(b[0:4:2]) # 0, 1, 2, 3을 찍는데 2씩 증가하면서 찍기, 따라서 0번과 2번이 나옴 (o ,a)
print(b[1:-2]) # -1은 뒤에서 첫번째, 따라서 r부터 g 미만이니 ran 
print(b[::-1]) # 전체범위를 -1 단위로, 즉 역순으로 출력 
