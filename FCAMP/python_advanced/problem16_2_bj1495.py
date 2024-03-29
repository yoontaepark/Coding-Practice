# 문제: 기타리스트 (백준 1495번)
# 한줄풀이: 음계 변경, 차례대로 곡을 연주 -> 동적 프로그래밍으로 해결 가능 (시간복잡도: O(NM))
# 모든 볼륨에 대해 연주 가능여부를 체크한다. 

# Day Of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다. 
# 지금까지 공연과는 다른 공연을 보여주기 위해서 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.

# 먼저, 공연이 시작하기 전에 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다. 
# 이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다. 
# 항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다. 즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i] 로 연주해야 한다. 
# 하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.

# 곡의 개수 N과 시작 볼륨 S, 그리고 M이 주어졌을 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오. 모든 곡은 리스트에 적힌 순서대로 연주해야 한다.

# 입력
# 첫째 줄에 N, S, M이 주어진다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 1000, 0 ≤ S ≤ M) 둘째 줄에는 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이가 주어진다. 이 값은 1보다 크거나 같고, M보다 작거나 같다.

# 출력
# 첫째 줄에 가능한 마지막 곡의 볼륨 중 최댓값을 출력한다. 만약 마지막 곡을 연주할 수 없다면 (중간에 볼륨 조절을 할 수 없다면) -1을 출력한다.

# 예제 입력 1 
# 3 5 10
# 5 3 7
# 예제 출력 1 
# 10

# 곡의 개수 n, 시작볼륨 s, 최대볼륨 m 을 각각 입력
n, s, m = map(int, input().split())

# 현재 볼륨에서 다음 곡이 시작하기 전에 줄 수 있는 볼륨 차이
array = list(map(int, input().split()))

# 처음 상태+곡의 개수만큼 행을 만들고, 그 행들에는 볼륨0부터 최대값(포함)까지 열을 만든다. 
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        # 해당 셀이 0 이면 위로 올라가서 for문(j) 다시 수행
        if dp[i-1][j] == 0:
            continue

        # 이전셀이 1인 경우에 대해서만 볼륨을 빼고 더해보면서 해당하면 해당 셀을 1로 바꿔준다
        if j-array[i-1] >= 0:
            dp[i][j-array[i-1]] = 1
        
        if j+array[i-1] <= m:
            dp[i][j+array[i-1]] = 1

# 마지막 곡 수행 후 결과값 기준으로 역순으로 for문 돌리면서 결과값이 있으면 바로 결과값 저장하고 for문 탈출 
result = -1
for i in range(m,-1,-1):
    if dp[n][i] == 1:
        result = i
        break

print(result)

