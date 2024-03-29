# 문제: 가장 긴 증가하는 부분수열 (백준 11053)
# 한줄풀이: 동적 프로그래밍 문제(O(n^2)), 비교해서 뒤에가 크면 비교한 값 + 1 해준다. 

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력 1 
# 6
# 10 20 10 30 20 50
# 예제 출력 1 
# 4

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

# 실제로는 n개를 비교하고 0번 인덱스부터 n-1번 인덱스까지 비교이기 때문에 (1,n) / (0,i) 로 인덱스 비교 
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))