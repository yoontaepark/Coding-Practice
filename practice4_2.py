# # 사전, dictionary, {}
# # 정수형으로 키값을 넣는 예시
# cabinet = {3:"유재석", 100:"김태호"} # key:value 식으로 값을 채워넣음
# print(cabinet[3])  # 데이터 부르는 방식은 [key]를 넣어서 조회한다
# print(cabinet[100])

# print(cabinet.get(3)) # 혹은 .get 함수를 써서 부를수도 있음. 이때는 ()를 씀

# # 있는 값을 부를경우에는 동일, 없는 값을 부를 경우 두개가 다름
# # print(cabinet[5]) # 이 경우 traceback 발생
# print(cabinet.get(5)) # 이 경우 에러는 안나고, None으로 출력됨
# print(cabinet.get(5, "없는 값임")) # None 호출되는게 싫으면 , 문자열 입력 가능

# # 키가 딕셔너리 안에 있는지 확인하는 방법 키 in 변수 로 검색 
# print(3 in cabinet) # True
# print(5 in cabinet) # False

# # string 형태로도 키값을 넣을 수 있음
# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])


# # 새 손님(한번 만든 이후에)
# cabinet["A-3"] = "김종국" # 있는 키값이면 Value가 덮어씌워짐
# cabinet["C-20"] = "조세호" # 없는 키값이면 키값과 대응하는 value 값을 신규 생성
# print(cabinet)

# # 간 손님(del 펑션 사용)
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력 
# print(cabinet.items())
# print(cabinet) #물론 그냥 출력하는거와 동일하게 나옴

# # 목욕탕 페점
# cabinet.clear()
# print(cabinet)

# ####################
# # 튜플, Tuple, 내용변경이나 추가를 할 수 없음, 속도가 list 보다 빠름
# menu = ("돈까스", "치즈까스") # ()형태로 표현함
# print(menu[0]) # 출력은 변수명[key]로

# #menu.add("생선까스") → 튜플 형태이기 때문에, 내용변경 시 에러가 남

# # 여러가지 변수를 한꺼번에 설정 가능
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)


# ################################
# # 집합(set)
# # 딕셔너리랑 비슷한 형태임, 중복 안됨, 순서 없음 
# my_set = {1,2,3,3,3}
# print(my_set) # 이 경우 1,2,3만 출력됨, 중복된 나머지 3은 삭제됨

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합(java and python), 변수&변수를 하던지, .intersection 사용
# print(java & python)
# print(java.intersection(python))

# # 합집합(or), 변수|변수를 하던지, .union 사용
# print(java | python)
# print(java.union(python))

# # 차집합(java o, python x 인 사람 찾기), 변수 - 변수를 하던지, .difference 사용
# print(java - python)
# print(java.difference(python))

# # 추가, 삭제
# # 추가는 .add, 삭제는 .remove

# python.add("박윤태")
# print(python)

# java.remove("김태호") #없는거 삭제 시 에러 호출됨
# print(java)


# 자료구조의 변경
# 자료형을 변경할 수 있음
menu = {"커피", "우유", "주스"} #현재는 set 형 일거임
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

menu = dict(menu)
print(menu, type(menu))

