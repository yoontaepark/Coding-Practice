# 문제: 해킹(백준 10282번)
# 한줄풀이: 최소시간을 구해라 -> 다익스트라 최단 경로 알고리즘 문제, 도달할 수 있는 정점들의 개수와 최대 거리를 출력, 우선순위 큐를 이용(O(NlogD))

# 최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다. 
# 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

# 최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 개수는 최대 100개이다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

# 첫째 줄에 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c가 주어진다(1 ≤ n ≤ 10,000, 1 ≤ d ≤ 100,000, 1 ≤ c ≤ n).
# 이어서 d개의 줄에 각 의존성을 나타내는 정수 a, b, s가 주어진다(1 ≤ a, b ≤ n, a ≠ b, 0 ≤ s ≤ 1,000). 
# 이는 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨을 뜻한다.
# 각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않는다.

# 출력
# 각 테스트 케이스마다 한 줄에 걸쳐 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력한다.

# 예제 입력 1 
# 2
# 3 2 2
# 2 1 5
# 3 2 5
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4

# 예제 출력 1 
# 2 5
# 3 6

# 다익스트라다? heapq 임포트해라
import heapq
import sys

def dijkstra(start):
    # 힙 초기화하고나서
    heap_data = []
    
    # (거리, 노드) 형태로 힙에 넣어둔다. 우선순위 큐라서 거리를 앞에 둬야 함. 처음이니까 시작점은 거리가 0
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0

    # 힙을 비울때까지
    while heap_data:
        # 다시꺼내서(거리, 노드)
        dist, now = heapq.heappop(heap_data)

        # 만약에 저장되어 있는 거리가 현재 넘어온 거리보다 작다면 아래 갈 필요가 없으니 다시 while문으로 올라감
        if distance[now] < dist:
            continue
        # adj에 넣은 튜플마다(즉, 지금 노드에서 연결된 노드들을 이제 업데이트)
        for i in adj[now]:
            # 거리를 업데이트 해준다. 
            cost = dist + i[1]
            # 연결되어 있는 노드까지의 거리를 cost로 업데이트하고, 힙에다가는 다시 (거리, 연결되어 있는 노드)를 넣는다.   
            # 우선순위 큐라서 cost부터 지정
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

# 메모리랑 시간을 단축시킬 수 있음
input = sys.stdin.readline


for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj = [[] for i in range(n+1)]
    distance = [float('inf')] * (n+1)
    
    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[y].append((x, cost))
    
    dijkstra(start)
    count = 0
    max_distance = 0
    for i in distance:
        if i != float('inf'):
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)
