# # 문자열 처리
# # 1) 문자열
# sentence = '나는 소년입니다' # '' 로 문자열 선언할 수 있음
# print(sentence)
# sentence2 = "파이썬은 쉬워요" # ""로도 문자열 선언할 수 있음
# print(sentence2)
# sentence3 = """  
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3) # 여러줄 표현시에는 """ """ 로 문자열 선언하기


# # 2) 슬라이싱
# jumin = "990120--1234567"

# print("성별: " + jumin[8]) # 첫글자 위치는 0(고정), 성별인 1의 위치는 8
# print("연: " + jumin[0:2]) # 0부터 2 직전까지, [from:to - 1] 이라고 보기
# print("월: " + jumin[2:4]) 
# print("일: " + jumin[4:6])

# print("생년월일: " + jumin[:6]) # 처음부터 6직전까지
# print("뒤7자리: " + jumin[8:]) # 총글자수가 0~14(포함), 8부터 끝까지
# print("뒤7자리: " + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지, 0은 안셈


# # 3) 문자열처리함수, 문자열.함수()로 구현한다
# sample = "Python is Amazing"
# print(sample.lower()) # 문자열 전체를 소문자로 출력
# print(sample.upper()) # 대문자로 출력
# print(sample[0].isupper()) # 특정 문자가 대문자인지 확인, 이경우 맞으니 True
# print(len(sample)) #문자열의 총 길이, 6+7+2+2(space) = 15
# print(sample.replace("Python", "Java")) # 바꾸고 싶은 부분을 변경, 원본 안바뀜

# sample2 = sample.index("n")
# print(sample2) # .index("특정문자") 특정문자가 몇번째에 위치해있는지, 5
# sample3 = sample.index("n", sample2 + 1)
# print(sample3) # 첫 문자를 찾은 위치+1 부터 찾으면, 두번째 위치를 찾을 수 있음
# sample4 = sample.index("n", 6)
# print(sample4) # 바로 위랑 똑같은 소리임 

# print(sample.find("Java")) # find는 없으면 -1로 출력
# # print(sample.index("Java")) # index는 없으면 traceback 임

# print(sample.count("n")) # n의 갯수를 카운팅


# 4) 문자열 포맷
# 방법 1
# print("나는 %d살입니다." % 20) # %d는 정수형만 받음, 뒤에 %정수 입력하면 됨
# print("나는 %s을 좋아해요." % "파이썬") # %s는 문자열(+ 다됨)
# print("Apple은 %c로 시작해요." % "파") # %c는 문자  

# # s%는 다 됨, 복수로 넣으려면 % 뒤에 ( , )로 표현. 이때 순차적으로 들어감
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색이 좋아요." % ("파란", "빨간")) 

# # 방법 2, {}를 넣고 뒤에 .format을 사용, 복수형 표현은 동일
# # {0},{1} 이런식으로 넘버링해도 됨, 이경우 넘버링으로 변수위치 조정가능
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3, {변수명} 넣고, .format뒤에 변수정의, 순서무관하게 정의한 변수를 읽음
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))
# print("나는 {age}살이며 {color}색을 좋아해요.".format(color="빨간", age=20))

# # 방법 4 (v3.6 이상~), 변수 먼저 정의한다음에 print문 앞에 f넣고 {변수}
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요.")


# # 5) 탈출문자
# # \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# # \" \' : 문장 내에서 따옴표
# # ex) 저는 "박윤태" 입니다. 
# # print("저는 "박윤태" 입니다.")  #에러가 남, """" 로 인식하기 때문
# print("저는 '박윤태' 입니다.")  # "" 내에 ''로 피할수는 있음 
# print('저는 "박윤태" 입니다.')  # 혹은 '' 내에 ""로 피할수는 있음 
# print("저는 \"박윤태\" 입니다.")  # 이런식으로 따옴표를 아예 \로 처리도 가능

# # \\: 문장 내에서 \ 
# # print("C:\Users\PC\Desktop\PythonWorkspace>") #파일경로 칠때 에러가 남
# print("C:\\Users\\PC\\Desktop\\PythonWorkspace>") #\\처리로 에러수정

# # \r : 이하 문자(열)을 맨 앞으로 이동하면서 겹쳐쓰기(insert 와 유사)
# print("RedApple\rPine") #Pinepple이 나옴(RedA가 지워짐)

# # \b : 백스페이스(바로 앞 한글자 삭제)
# print("Reda\bApple") # RedApple이 나옴

# # \t : 탭(말그대로 tab임)
# print("Red\tApple")


'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1: http://부분은 제외 → naver.com 
규칙2: 처음만나는 점(.) 이후 부분은 제외 → naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!' 로 구성

예) 생성된 비밀번호: nav51!
'''

# Answer
var = "http://naver.com"
rule1 = var[7:-4]
# print(rule1)
rule2 = rule1[:3]
# print(rule2)
rule3 = len(rule1)
# print(rule3)
rule4 = rule1.count("e")
# print(rule4)
pwd = str(rule2) + str(rule3) + str(rule4) + "!"
print(pwd)

# 동영상 풀이
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1 부분, 아예 replace 함수를 쓰자
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] 랑 동일한 의미가 되고, 0~5직전까지를 의미함
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
 


