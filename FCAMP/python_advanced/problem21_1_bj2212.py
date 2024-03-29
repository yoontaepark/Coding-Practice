# 문제: 센서 (백준 2212번)
# 한줄풀이: 각 센서 사이의 거리를 계산(x->y 이면서 집중국을 x에 놨을 때 y까지의 거리), 가장 거리가 긴부분을 0으로 설정해서 연결을 끊어버린 후, 
# 각 묶음별 거리를 합치면 된다. 

# 한국도로공사는 고속도로의 유비쿼터스화를 위해 고속도로 위에 N개의 센서를 설치하였다. 
# 문제는 이 센서들이 수집한 자료들을 모으고 분석할 몇 개의 집중국을 세우는 일인데, 예산상의 문제로, 고속도로 위에 최대 K개의 집중국을 세울 수 있다고 한다.

# 각 집중국은 센서의 수신 가능 영역을 조절할 수 있다. 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다. 
# N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.

# 편의를 위해 고속도로는 평면상의 직선이라고 가정하고, 센서들은 이 직선 위의 한 기점인 원점으로부터의 정수 거리의 위치에 놓여 있다고 하자. 
# 따라서, 각 센서의 좌표는 정수 하나로 표현된다. 이 상황에서 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오. 
# 단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

# 입력
# 첫째 줄에 센서의 개수 N(1<=N<=10,000), 둘째 줄에 집중국의 개수 K(1<=K<=1000)가 주어진다. 셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 
# 각 좌표 사이에는 빈 칸이 하나 이상 있으며, 좌표의 절댓값은 1,000,000 이하이다.

# 출력
# 첫째 줄에 문제에서 설명한 최대 K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값을 출력한다.

# 예제 입력 1 
# 6
# 2
# 1 6 9 3 6 7

# 예제 출력 1 
# 5

import sys

n = int(input())
k = int(input())

# 집중국의 개수가 센서이상이면 정답은 0
if k >= n:
    print(0)
    sys.exit()

# 모든 센서의 위치를 입력 받아 오름차순 정렬
array = list(map(int, input().split(' ')))
array.sort()

# 각 센서간의 거리를 계산해서 내림차순 정렬
distances = []
for i in range(1, n):
    distances.append(array[i] - array[i-1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k-1):
    distances[i] = 0
print(sum(distances))
