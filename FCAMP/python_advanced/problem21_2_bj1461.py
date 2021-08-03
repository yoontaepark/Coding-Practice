# 문제: 도서관 (백준 1461번)
# 한줄풀이: 0보다 큰 / 작은 책들을 나누어 처리, 가장 먼 책을 마지막으로 놓기(돌아올 필요없으니)
# 묶음중에 가장 거리가 먼 책만큼 이동해야함, 왕복거리 구한다음에 가장 긴 거리어치 편도만 차감

# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 
# 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 
# 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

# 입력
# 첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다. 둘째 줄에는 책의 위치가 주어진다. 
# N은 10,000보다 작거나 같은 자연수이고, M은 10,000보다 작거나 같다. 책의 위치는 0이 아니며, 그 절댓값이 10,000보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

# 예제 입력 1 
# 7 2
# -37 2 -6 -39 -29 11 -28

# 예제 출력 1 
# 131

import heapq

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
positive = []
negative = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(array), -min(array))

# 최대 힙을 위해 원소를 음수로 구성(우선순위 큐는 최소 힙이기 때문)
for i in array:
    if i > 0:
        heapq.heappush(positive, -i)
    else:
        heapq.heappush(negative, i)

result = 0

while positive:
    # m개씩 빼기
    result += heapq.heappop(positive)
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    # m개씩 빼기
    result += heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

# 가장 먼곳을 차감
print(-result * 2 - largest)



