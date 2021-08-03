# 문제: 숨바꼭질 (백준 1697번)
# 한줄풀이: 그래프 문제, DFS/BFS 문제, 이건 BFS로 풀자(재귀 특성상 시간복잡도가 좀더 높아서 BFS를 더 선호)


# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4

from collections import deque

# Max 값 우선 설정
MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

# 큐만든다음에
def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        # 찾는값과 같으면 해당 인덱스의 값을 출력
        if now_pos == k:
            return array[now_pos]

        # 세가지 이동방향에 대해 반복하면서
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            # 인덱스가 범위안에 있거나, 0이 아닌 경우에 대해서만 어레이값을 1 더해주고 다시 큐에 넣는다. 
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)

print(bfs())
