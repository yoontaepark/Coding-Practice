# 문제: 중량제한 (백준 1939번)
# 한줄 풀이: 

# N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

# 영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 
# 물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 
# 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, M(1≤M≤100,000)이 주어진다. 
# 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1≤A, B≤N), C(1≤C≤1,000,000,000)가 주어진다. 
# 이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다.
# 서로 같은 두 도시 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 
# 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 
# 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.

# 출력
# 첫째 줄에 답을 출력한다.

# 예제 입력 1 
# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3
# 예제 출력 1 
# 3

# 양쪽으로 뚤려있는 큐를 사용하기 위해 라이브러리 호출
from collections import deque

# 넓이우선탐색 함수
def bfs(c):
    # 큐 생성
    queue = deque([start_node])
    
    # 모든 노드들을 일단 False 로 초기화 
    visited = [False] * (n+1)
    # 시작점은 시작이기 때문에 True로 변경
    visited[start_node] = True

    # 큐가 다 빌때까지 반복
    while queue:
        # 가장 좌측 값을 뽑아서
        x = queue.popleft()
        # 그 값에 해당하는 좌표들(즉, x에서 나머지 노드들과 거리)를 반복
        for y, weight in adj[x]:
            # 이동할 노드가 False이고 무게가 원하는 무게(c) 보다 크다면
            if not visited[y] and weight >= c:
                # 노드를 방문했다 라고 보고 True로 변경
                visited[y] = True
                # 방문한 노드 부터 또 다시 큐를 돌리기 위해 추가
                queue.append(y)

    # 다 돌리고 나서 실제로 도달하고자하는 노드의 어레이 인덱스번호를 리턴받아보면 됨. 못갔으면 False // 갔으면 True
    return visited[end_node]

# 노드, 다리 개수를 입력하고
n, m = map(int, input().split())

# 그냥 배열 초기화 했다고 볼 것 
adj = [[] for _ in range(n+1)]

# 특이하게도 시작점을 max값, 도착점을 min값으로 초기화한다
start = 1000000000
end = 1

# 다리 개수만큼 반복하는데
for _ in range(m):

    # 입력을 받아서
    x, y, weight = map(int, input().split())

    # array x번 기준으로는 (y, weight) // y번 기준으로 (x, weight)이 들어감 (즉, 쌍방으로 들어가게 됨)
    adj[x].append((y,weight))
    adj[y].append((x,weight))

    # 시작점을 아까 max 범위의 값과 weight과 비교해서 min 값 // 도착점은 그 반대로 
    start = min(start, weight)
    end = max(end, weight)

# 시작노드와 끝 노드 확인
start_node, end_node = map(int, input().split())

# 일단 결과값은 최소 무게 이상일테니 최소 무게로 초기화
result = start

# 시작점이 끝점보다 클때까지 반복
while(start <= end):
    # 이진탐색을 사용한다. mid값 설정하는 모습
    mid = (start + end) // 2

    # bfs로 탐색을 잘했으면(통과했으면), 결과값을 업데이트 치되, 시작점을 올려본다. (즉, 무게를 올려본다)
    if bfs(mid):
        result = mid
        start = mid + 1
    
    # 탐색을 못했으면 답이 아니기 때문에 result값(무게)은 변동없고, 끝점을 내려본다.(즉, 무게를 내려본다) 
    else:
        end = mid - 1

# 결과값 출력
print(result) 
    
