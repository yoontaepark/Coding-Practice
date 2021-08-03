# 과제3.
# n개의 노드가 있는 그래프가 있다. 각 노드는 1부터 n까지 번호가 적혀있다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 한다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성하라.

# 제한사항

# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
# 입출력 예

# n	vertex	                                                    return
# 6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

def solution(n, vertex):

    # initialize
    arr = [[] for _ in range(6)]
    visit = [0 for _ in range(6)]
    distance = [0 for _ in range(6)]
    answer = 0

    # arr배열을 만들어서, 각 노드번호가 어느 노드들을 가리키고 있는지 저장
    for i in vertex:
        x = i[0] - 1
        y = i[1] - 1
        arr[x].append(y)
        arr[y].append(x)

    # pop할 첫 큐 초기화, 첫 노드는 방문횟수를 1로 초기화
    q = [0]
    visit[0] = 1

    # pop이 끝날때까지 while문 반복
    while q:
        # 가장 첫번째(왼쪽) 값을 pop한다
        x = q.pop(0)

        # pop한 인덱스를 for문으로 돌리면서 거리를 추가
        for i in arr[x]:
            # 방문횟수가 아예 없다면 1로 바꿔주면서 큐에 넣는다
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)

                # 방문횟수가 늘어나면 거리도 1 늘려준다. 단, 노드 1번에서의 거리를 재야하기 때문에, 1부터 연결된 이전 노드까지의 거리 + 1 로 해줘야 함
                distance[i] = distance[x] + 1
    
    # distance의 max를 뽑고 그 max 개수를 저장 및 리턴
    answer = distance.count(max(distance))
    return answer
                


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, vertex))
