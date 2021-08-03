# 문제: N-Queen (백준 9663번)
# 한줄풀이: 백트래킹, 완전탐색, DFS, 각 행마다 dfs를 돌리면서 각열에 퀸을 놓는 경우를 고려(이 때 위쪽 행을 모두 확인)

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 예제 입력 1 
# 8
# 예제 출력 1 
# 92

# x번째 행에 놓은 퀸에 대한 검증
def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

# x번째 행에 대한 처리, 재귀는 아니고 그냥 0번부터 - 1 - 2 - 3 에 대한 모든 경우의수를 돌리면서 성립할때만(x+1 = n 으로 넘어가는 순간) result에 1 더해줌
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # x번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            # 해당 위치에 Queen을 두어도 괜찮은 경우 
            if check(x):
                # 다음 행으로 이동 
                dfs(x+1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)