# 문제: 베스트셀러 (백준 1302번)
# 한줄 풀이: 등장횟수 계산은 딕셔너리를 이용하면 좋음 

# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 
# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

# 예제 입력 1 
# 5
# top
# top
# top
# top
# kimtop
# 예제 출력 1 
# top

n = int(input())

books = {}

# 참고로 인덱스처럼 넣어서 값을 넣는것 처럼 보이지만, 인덱스가 아님. {'key': 'value'} 이렇게 들어가 있음 
for _ in range(n):
    book = input()
    # 딕셔너리에 없으면 벨류를 1로 해서 생성해
    if book not in books:
        books[book] = 1
    # 이미 있으면 벨류를 1 더해
    else:
        books[book] += 1

# 벨류 중 가장큰 값을 새롭게 정의(이경우 숫자가 됨)
target = max(books.values())
array = []

# key, value 둘다 뽑은다음에
for book, number in books.items():
    # value가 목표와 같은 값이면 key값을 어레이에 추가// 루프를 돌리니 max가 중복이면 어레이에 추가가 될 것
    if number == target:
        array.append(book)

# sorted 를 하고나서 0번째 인덱스를 출력해라! 
print(sorted(array)[0])    
        