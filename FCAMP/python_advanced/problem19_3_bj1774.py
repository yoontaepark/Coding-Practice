# 문제: 우주신과의 교감(백준 1774번)
# 한줄풀이: 정점을 다 이어라 -> 최소신장트리 -> 크루스칼 알고리즘으로 풀자

# 황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 
# 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다. 
# 이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.

# 하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 
# 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.

# 우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 
# 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 
# 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.

# 또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 
# 통로들의 길이는 2차원 좌표계상의 거리와 같다.

# 이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 
# 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 
# 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

# 입력
# 첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.

# 두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다. 
# 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

# 출력
# 첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라. 출력은 소수점 둘째짜리까지 출력하여라.

# 예제 입력 1 
# 4 1
# 1 1
# 3 1
# 2 3
# 4 3
# 1 4
# 예제 출력 1 
# 4.00

# 힌트
# (1,1) (3,1) (2,3) (4,3) 이렇게 우주신들과 황선자씨의 좌표가 주어졌고 1번하고 4번이 연결되어 있다. 
# 그렇다면 1번하고 2번을 잇는 통로를 만들고 3번하고 4번을 잇는 통로를 만들면 신들과 선자씨끼리 다 도달이 가능하면서 더 만들어야 할 통로의 길이는 최소가 된다.

import math
import sys
input = sys.stdin.readline

def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a*a) + (b*b))

# 부모를 가져옴, 부모인 경우 값을 출력
def get_parent(parent, n):
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n])

# 작은놈을 부모로 
def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모가 같은지 확인
def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False

# 초기화
edges = []
parent = {}
locations = []

# 우주선 개수, 통로 개수
n, m = map(int, input().split())

# 우주선 개수마다 로케이션 정보를 넣어줌
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x,y))

length = len(locations)

# 좌표간 거리를 edges에 기록, 편의상 인덱스번호로 안하고 그냥 1,2 번호로 
for i in range(length - 1):
    for j in range(i+1, length):
        edges.append((i+1, j+1, get_distance(locations[i], locations[j])))

# 각 숫자의 부모는 숫자로 우선 초기화
for i in range(1, n+1):
    parent[i] = i

# 이미 순서쌍이 있으면 이어주기
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 거리순으로 소트해서 이어주기
edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
    # 둘의 부모가 같으면 연결하지 말기 
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print('%0.2f' % result)



