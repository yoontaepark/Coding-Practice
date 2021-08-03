# 과제5.
# 그래프를 DFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 start가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력: start부터 방문된 점을 순서대로 출력한다.

# 예시 입출력

# N	M	start	edges	출력
# 4	5	1	[[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]	1 2 3 4


# 과제 5번 코드란
N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]


def solution(N, M, V, edges):
    visited = [False] * (N+1)
    adj = [[] for _ in range(N+1)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    
    for e in adj:
        e.sort()
    
    def dfs(start):
        print(start, end=' ')
        visited[start] = True
        for e in adj[start]:
            if not visited[e]:
                dfs(e)

    dfs(V)

solution(N, M, V, edges)