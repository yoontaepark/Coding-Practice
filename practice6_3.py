# 지역변수와 전역변수
# 보통 전역변수를 선언한다음에 함수안에 (전역변수)를 넣고 함수내에서 return을 시켜서 다시 전역변수를 업데이트 하도록 한다. 

# # Case 1, 지역변수를 선언하고 return을 안 넣는 경우: 지역변수 따로, 전역변수 따로 값이 먹는다. 
# gun = 10 # 전역변수 

# def checkpoint(soldiers): # 경계근무
#     gun = 20 # 지역변수로 선언조차 안하면 에러가 남, 지역변수도 초기화가 안되어 있으니 아래 gun을 사용할 수가 없음
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("[함수 밖] 전체 총 : {0}".format(gun))  # 처음 선언한 전역변수 10을 끌고 옴
# checkpoint(2) # 함수 안의 print문을 출력, 이때 지역변수 'gun'을 사용하므로 18이 나옴
# print("[함수 밖] 전체 총 : {0}".format(gun)) 
# # 처음 선언한 전역변수 10을 다시 끌고 옴, 함수가 리턴하는 값이 없기 때문에, 전역변수의 값은 변하지 않는다. 
# # (다시말해, 지역변수의 값을 return 시켜야 전역변수랑 동기화가 된다)


# Case 2, 함수 내 전역변수를 끌고오게끔 한다. 리턴은 아직 안넣은 상태인 경우
# 되긴 하는데, 지역변수 자리에 전역변수를 끌고오는 방식으로는 잘 안한다. 
# gun = 10 # 전역변수 

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용, 사실 이렇게는 잘 안쓴다. 
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("[함수 밖] 전체 총 : {0}".format(gun)) # 10
# checkpoint(2) # 8 
# print("[함수 밖] 전체 총 : {0}".format(gun)) # 8


# Case 3, 권장되는 방법, 함수안에 파라미터를 넣고, 리턴도 해준다 
gun = 10 # 전역변수

def checkpoint_ret(gun, soldiers): # 함수의 전달값으로 변수를 던진다음에 리턴도 받는다. 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("[함수 밖] 전체 총 : {0}".format(gun)) # 10
gun = checkpoint_ret(gun, 2) # 8, 리턴된 값을 받을 수 있도록 변수명 = 함수값으로 지정하기 
print("[함수 밖] 전체 총 : {0}".format(gun)) # 8