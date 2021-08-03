# 문제: 효율적인 해킹(백준 1325번)
# 한줄풀이: 모든 정점에 대해 DFS OR BFS를 수행, 방문하게 되는 노드의 개수 중 가장 큰 시작정점을 출력 

# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 
# 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

# 출력
# 첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

# 예제 입력 1 
# 5 4
# 3 1
# 3 2
# 4 3
# 5 3
# 예제 출력 1 
# 1 2

from collections import deque

def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    count = 1

    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    
    return count

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

# x가 y를 신뢰한다. y를 해킹하면 -> x도 해킹할 수 있다. 따라서 y 인덱스에 x를 넣어두면 된다. (일방)
for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

result = []
max_value = -1

# count 개수를 저장해서 max 값이랑 비교하고 result 배열에 넣어둔다. 
for i in range(1, n+1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

# 그리고 출력
for e in result:
    print(e, end=' ')