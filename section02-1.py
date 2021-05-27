# Print 함수의 다양한 사용방법
# Print
# 1. 가장 기본적인 output(출력) 함수
# 2. 기본 출력
# 3. Seperator, End 옵션 사용
# 4. Format 형식 출력
# 5. Escape Code 사용법

# Section02-1
# 파이썬 기초 코딩
# Print 구분의 이해 

# 기본출력
print('Hello python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

print()

# Seperator 옵션 사용
# 출력하는 항목들 사이에 뭘 넣겠다/혹은 안넣겠다 라는 뜻
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# End 옵션 사용, 끝에 뭘 넣겠다는 뜻이면서 아래 print함수를 한줄로 이어주는 역할
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용: [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('Yoon', 7))

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

'''
참고: Escape 코드

\n: 개행(엔터)
\t: 탭
\\: 문자로 인식
\': 문자
\": 문자
\r: 캐리지 리턴
\f: 폼 피드
\a: 벨소리
\b: 백 스페이스
\000: null 문자

'''

print("'you'")
print('\'you\'')
print('"you"')
print("""'you""")
print('\\you\\\n\n\n\n\n\n')
print('\t\ttest')