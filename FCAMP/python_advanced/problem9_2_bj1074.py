# 문제: Z (백준 1074번)
# 한줄 풀이: 재귀함수로 4개씩 묶어서 풀기
# Updata: 재귀함수가 시간초과가 뜸, 따라서 재귀로 돌리지말고 유사재귀로 n을 1씩 감소시키면서 필요한 사분면만큼의 숫자를 더해주자

# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# 만약, N > 1이 라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
# 다음은 N=3일 때의 예이다.

# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.

# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.

# 제한
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2N

n,r,c = map(int, input().split(' '))
result = 0
while n > 0:
    temp = (2 ** n) // 2
    if n > 1:
        # 2사분면에 있다면 (r <2 이어야, c >= 2면 됨)
        if temp > r and temp <= c:
            # 1사분면을 날리고
            result += temp ** 2
            # y좌표(열)를 1사분면으로 땡긴다. 
            c -= temp
        
        # 3사분면에 있다면(temp가 딱 중앙이 아니어서 그런데, temp를 2라고 하면 r >= 2, c < 2 여야 3사분면)
        elif temp <= r and temp > c:
            # 3사분면을 날리고
            result += (temp ** 2) * 2
            # x좌표(행)를 1사분면으로 올린다
            r -= temp

        # 4사분면에 있다면(temp가 딱 중앙이 아니어서 그런데, temp를 2라고 하면 r >= 2, c >= 2 여야 4사분면)
        elif temp <= r and temp <= c:
            # 4사분면을 날리고
            result += (temp ** 2) * 3
            # x좌표(행), y좌표(열)를 1사분면으로 올린다
            c -= temp
            r -= temp

    # 마지막 1사분면에 값을 몰아놓고 정리
    if n == 1:
        # 2번째 칸이라면 1을 더한다
        if r == 0 and c == 1:
            result += 1
        # 3번째 칸이라면 2를 더한다
        elif r == 1 and c == 0:
            result += 2
        # 4번째 칸이라면 3을 더한다. 참고로 1번째 칸이었다면 0을 더하면 되기 때문에 생략한다. 
        elif r == 1 and c == 1:
            result += 3
    
    n -= 1

print(result)




# 지금 버젼에서는 재귀가 에러가 난다.
# import sys

# def solve(n, x, y):

#     # 전역변수를 사용해서
#     global result
#     # 2x2 행렬일때만 
#     if n == 2:
#         # (0,0), (0,1), (1,0), (1,1) 에서 조건 안걸리면 result에 +1, 즉 연관없으면 4가 더해진다. 
#         # 0에서 시작해서, 첫번쨰꺼가 맞으면 0, 두번째꺼가 맞으면 1, 세번째꺼가 맞으면 2, 네번째꺼가 맞으면 3
#         # 넷다 아니면 4로 넘어가서, 다시 첫번째꺼가 맞으면 4, 2nd = 5, 3rd = 6, 4th = 7 이렇게 간다.
#         if x == X and y == Y:
#             print(result)
#             exit(0)
#         result += 1
        
#         if x == X and y+1 == Y:
#             print(result)
#             exit(0)
#         result += 1
        
#         if x+1 == X and y == Y:
#             print(result)
#             exit(0)
#         result += 1
        
#         if x+1 == X and y+1 == Y:
#             print(result)
#             exit(0)        
#         result += 1
#         return 
    
#     solve(n/2, x, y)
#     solve(n/2, x, y + n/2)
#     solve(n/2, x + n/2, y)
#     solve(n/2, x + n/2, y + n/2)
        

# result = 0
# N, X, Y = map(int, sys.stdin.readline().split(' '))
# solve(2**N, 0, 0)

