# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('\n')

# 문자형 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9) #놀랍게도 아래와 같이 문자 * 숫자를 해도 된다
print('\n')

# Boolean(참/거짓)
print(5>10)
print(10>5)
print(True)
print(False)
print(not True)
print(not (5>10))
print('\n')

# 변수, 애완동물을 소개해 주세요~
animal = "고양이"
name = "헤피"
age = 4
hobby = "낮잠"
is_adult = age >= 3


print("우리집 " + animal +"의 이름은 " + name + "에요")
hobby = "공놀이" #변수를 출력문 직전에 변경한다면, 바뀐 값이 반영됨

# 정수형을 출력할때에는 문자형, str()로 감싸줘야 에러가 안남. 
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") 

# +로 변수와 문자/숫자를 섞어 쓸수도 있지만, ,로 대체가능
# ,를 쓰면 변수에 str 씌울 필요는 없어지지만, 기본적으로 한칸 띄어쓰기 해야함
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") 

# Boolean형도 출력할 때 str()로 감싸줘야 에러가 안남
print(name + "는 어른일까요? "+ str(is_adult)+"\n")

# 주석처리하려면, # 쓰면 됨(한줄짜리), 단축키로는 ctrl+/(설정/해제 가능)
# 혹은 ''' 내용~~~ ''' 로 다중 주석처리도 가능
'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오
변수명: station
변수값: "사당", "신도림", "인천공항" 순서대로 입력
출력문장: xx행 열차가 들어오고 있습니다. 
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다")