# 리스트, list, []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10, subway2 = 20, subway3 = 30

subway = [10, 20, 30] # []에 넣고싶은만큼 변수를 넣으면 됨, 자료형 섞어도 됨
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)


# 조세호씨가 몇번째 칸에 타고 있는가? → .index 함수를 사용
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐 → .append 함수를 사용
subway.append("하하")
print(subway)

# 정형돈씨를 유재석/조세호 사이에 태워봄 → .insert 함수를 사용 / (위치, 오브젝트)
subway.insert(1, "정형돈")  # 1번 칸에 넣고 나머지는 뒤로 밀림
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 → .pop 함수를 사용
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능  → .sort()
num_list = [5,4,2,1,3]
num_list.sort()  #기본적으로는 오름차순 정렬임
print(num_list)

# 순서 뒤집기 가능 → .reverse()
num_list.reverse()
print(num_list)

# 모두 지우기 → .clear()
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
num_list = [5,4,2,1,3]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 → .extend(변수명), 정확히는 iterable 이 들어감(list, str, tuple)
mix_list.extend(num_list)
print(mix_list)
