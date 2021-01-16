##함수, def 함수명(): 실제 수행할 내용을 적는다. 호출할 때까지 나타나지는 않음
# 함수일반, 전달값과 반환값
def open_account(): # 함수를 정의, 이 함수는 호출될 때까지 나타나지는 않음, 이 함수는 리턴하는 값은 없음
    print("새로운 계좌가 생성되었습니다.")  # 함수가 호출되었을 때 수행할 내용

open_account() # 함수를 실제로 호출하는 모습


def deposit(balance, money): # 함수안에 (전달할 값) 을 넣는 경우도 있음, 이 경우 함수로 값이 전달되어 수행됨
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money # 함수 실행 후 리턴값을 던져줌

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다.")
        return balance

def withdraw_midnight(balance, money):
    commission = 80
    return commission, balance - money - commission # 리턴받을 값을 복수개로 지정할 수도 있음


balance = 0 
balance = deposit(balance, 1000) 
# 함수 실행 후에 리턴값이 없다면, balance = 0 을 유지할 것이었으나 리턴값이 있으니 1000원이 됨
# 그리고, 위처럼 변수 = 함수로 정의하는 경우에는 변수에 리턴값을 묻어줘야 에러가 안남 (일단 이정도만 받아들이기)
# print(balance)
balance = withdraw(balance, 400) # 이 경우 if 조건문이 실행되면서 balance 변수에 balance - money 값을 출력한다
# balance = withdraw(balance, 2000) # 이 경우 else 조건문이 실행되면서 balance 변수에 balance 값을 출력한다. 

# commission = withdraw_midnight(balance, 500) # 리턴받을 변수를 하나로만 지정하면 튜플 형태로 나옴 (80,20)
commission, balance = withdraw_midnight(balance, 500) # 리턴받을 변수를 두개로 지정해서 각각의 값을 리턴받는 모습

print("수수료는 {0}원, 잔액은 {1}원 입니다.".format(commission, balance)) # {0} 자리와 {1} 자리에 각각 80, 20 이 들어감 


# 기본값: 함수안에 전달할 값을 넣는데 거기에 기본값까지 세팅해줄수도 있음 
# 일단 기본값을 안넣는 경우
def profile(name, age, main_lang): 
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))   # 두줄로 쓰고 싶으면 \를 적고나서 엔터치면 된다

profile("유재석", 20, "파이썬")
profile("김태호", 30, "자바")

# 기본값을 넣는 경우, 이 경우 같은 나이와 같은 사용언어라고 가정하면 
def profile2(name, age = 17, main_lang = "파이썬"):  # age와 lang에 기본값을 넣었음
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))   

profile2("유재석")  # name 만 입력해도 나머지는 default값이 따라옴
profile2("김태호", 20) # 물론 이렇게 추가입력하면 추가입력한 값으로 덮어씌워짐

# 키워드 값을 이용한 함수 호출
# 매개변수에 키값을 미리 넣어두면 매개변수끼리 순서가 바뀌어도, 정의된 순서대로 값이 출력된다. 
def profile3(name, age, main_lang):
    print(name, age, main_lang)

profile3(name = "유재석", main_lang = "C++", age = 20)
profile3(main_lang = "JAVA", age = 40, name = "김태호")

