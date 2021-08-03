# 문제: DFS와 BFS (백준 1260번)
# 한줄풀이: 그래프 문제, DFS/BFS 문제, 정형화 되어 있기 때문에 암기 (시간복잡도: O(n^2))
# DFS는 재귀(이론적으로는 스택을 씀), BFS는 큐를 활용해서 수행


# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4

from collections import deque

# 깊이우선탐색은 일단 처음을 출력/방문했음으로 돌려놓고, 해당 정점에 연결되어 있는 정점들을 재귀로 다시 수행
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

# 넓이우선탐색은 우선 처음을 큐에 넣은다음에 큐가 빌때까지 반복, 처음 넣은 큐를 빼고/방문했음으로 돌리고/출력
# 마찬가지로 해당 큐에 엮여있는 정점들을 돌리면서, 방문안했으면 q에 append. 이러면 while문이 다시 돈다.  
# 참고로 먼저 들어가있는놈들부터 빠져나감
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

# 정점, 간선, 시작번호
n, m, v = map(int, input().split())

# 각각의 인덱스번호마다 간선으로 이어져있는 정점을 저장. 0번 인덱스는 안쓰고 n번 인덱스 쓸거니까 0~n+1 로 range 설정
adj = [[] for _ in range(n+1)]

# x,y를 넣을 때마다, x번째 인덱스에 y를 넣고, y번째 인덱스에 x를 넣는다. 
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# adj 각 배열인덱스에 들어가있는 배열들을 오름차순으로 정렬
for e in adj:
    e.sort()


# 방문여부로 dfs/bfs 수행
visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)