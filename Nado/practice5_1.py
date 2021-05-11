## 제어문
# if: 조건문, 조건에 따라 분기되는 결과문들을 만들면 됨

weather = input("오늘 날씨는 어때요? ") # input: 사용자 입력커서가 가장 오른편에 뜸
# 파이썬에서 결과문 쓸 때 띄어쓰기 제한은 없으나 tab으로 구분 (다른 언어가 그렇게 하니)
# if 조건문:, elif, else 순서로 씀. else는 안써도 되는데, 뭐라도 출력문을 만들려고 구성해놓으면 좋긴 함
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")  
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")
 

# 정수형 조건문, input 값을 정수형으로 변환
temp = int(input("기온이 몇도인가요?")) 
if temp >= 30:
    print("너무 더워요")
elif temp >= 10 and temp <30:
    print("Good weather")
elif 0 <= temp < 10:    # 파이썬 한정, 왼쪽처럼 from to를 한번에 넣을 수 있음
    print("외투를 챙기세요")
else:
    print("너무 추워요")

## for: 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# 위와 같이 반복적으로 print문을 찍는 경우 for문을 쓰면 됨
for waiting_no in range(5): #~0부터 5미만 이라는 소리임
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1,6): #range에 ~이상, ~미만 조건을 넣어도 됨
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "캡틴 아메리카"]
for customer in starbucks:
    print("{0}, your coffee is ready".format(customer))


## while문: 조건+반복문, 조건에 맞을때까지 반복
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다")

# #조건이 없어지면(무조건 반복하니까) 루프가 형성됨
# customer2 = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer2, index))
#     index += 1
# 참고) ctrl+c : 루프돌때 멈추는 기능

# while문 활용, 올바른 답변이 나왔을 때 반복을 멈추게끔 
customer3 = "Yoon"
person = "Unknown"
while person != customer3:
    print("{0}, 커피가 준비 되었습니다.".format(customer3))
    person = input("이름이 어떻게 되세요? ") 
    # person을 customer3과 맞을때까지 반복문이 돈다. 맞추면 아래 print 문으로 이동
print("커피 맛있게 드세요")
