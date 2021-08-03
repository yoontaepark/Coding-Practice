# 문제: 음계 (백준 2920번)
# 한줄풀이: 상향/하향을 True로 놓고, 배열을 한개씩 비교하면서 상태값을 바꿔준다. 

# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

# 예제 입력 1 
# 1 2 3 4 5 6 7 8
# 예제 출력 1 
# ascending

# 예제 입력 2 
# 8 7 6 5 4 3 2 1
# 예제 출력 2 
# descending

# 예제 입력 3 
# 8 1 7 2 6 3 5 4
# 예제 출력 3 
# mixed

# 입력을 한칸씩 띄어서 하고 엔터를 하면 리스트로 모아줌, 그리고 int형으로 변환시킴
a = list(map(int, input().split(' ')))

# 상승/하락에 대한 변수를 True로 초기화 함
ascending = True
descending = True

# 인덱스가 0~7이니까, 1~7로 반복문 돌리면서 (1,0) -> (7,6)
for i in range(1,8):
    # 하나라도 틀리면 내림차순이 아니다 + 이걸 다 통과하면 오름차순이다
    if a[i] > a[i-1]:
        descending = False
    # 하나라도 틀리면 오름차순이 아니다 + 이걸 다 통과하면 내림차순이다
    elif a[i] < a[i-1]:
        ascending = False


# 정리된 결과로, 각각이 true일 경우 결과값을 출력한다. 
if ascending: 
    print('ascending')
elif descending: 
    print('descending')
else:
    print('mixed')    
