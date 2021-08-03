# 문제: 공유기 설치 (백준 2110번)
# 한줄 풀이: 데이터가 너무 크다? -> 이진 탐색(왜냐면 시간복잡도가 바로 log(n)이 되니깐)

# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# 예제 입력 1 
# 5 3
# 1
# 2
# 8
# 4
# 9
# 예제 출력 1 
# 3

n, c = list(map(int, input().split(' ')))

array = []
# 집의 좌표를 오름차순으로 정렬
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = 1 # 최소 gap 
end = array[-1] - array[0]  # 최대 gap
result = 0

# 시작점이 끝점을 넘어가면 루프종료
while (start <= end):
    # 두 공유기 사이의 거리를 이진 탐색이니까 (최소+최대) // 2로 두고 시작
    mid = (start + end) // 2 # gap
    
    # 1번 인덱스
    value = array[0]

    # 1번 인덱스 본인에 한칸 설치
    count = 1
    
    # 2번 인덱스부터 끝까지 루프돌리면서
    for i in range(1, len(array)):

        # 2번 인덱스 값이 1번 인덱스 값 + gap 보다 크거나 같으면 설치가능하니
        if array[i] >= value + mid:
            # 설치하고, 해당 값을 기준점 value로 업데이트 
            value = array[i]
            count += 1
    
    # 위의 결과를 보고나서, 설치를 원하는거보다 많거나 같게 했으면, 최소 gap을 증가시키는데 이진탐색이니까 mid 지점+1부터 한다
    # 그리고 결과는 mid 값으로 저장 (두 공유기 사이의 거리임)
    if count >= c:
        start = mid + 1
        result = mid
    # 설치를 적게 했다면, 최대 거리를 줄여보는데 mid 기준으로 줄인다. 
    else:
        end = mid-1

print(result)
