# 문제: 수 정렬하기3(백준 10989번)
# 한줄풀이: 계수 정렬 사용, 0~9 배열을 만들고 거기에 카운팅을 해서 각각의 배열인덱스를 카운팅된만큼 출력한다. 
# 백준 1427 이랑 비슷함. + 수의 범위가 제한적일 때 계수정렬 사용
# 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline() 을 사용한다. 

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1 
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7

import sys

# 데이터 입력시 데이터 초과를 줄여주기 위한 입력 함수
n = int(sys.stdin.readline())
# array 에 1~10000까지 있을테니까 0 포함해서 10001개를 만들고 0으로 초기화
array = [0] * 10001

# 입력하고 할때마다 그 데이터에 해당하는 인덱스에 값을 +1
for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

# 0부터 10000까지 루프돌면서 그 값이 0이 아니라면 입력된 값만큼 반복해서 출력을 해준다. 
for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)





# 번외: 이거는 1427번 문제처럼 푼건데, 이게 안된다는건 아님. 데이터 초과가 뜸
# import sys

# n = int(sys.stdin.readline())
# array = []

# for i in range(n):
#     data = int(sys.stdin.readline())
#     array.append(data)


# for i in range(1, 10001):
#     for j in array:
#         if int(j) == i:
#             print(i) 