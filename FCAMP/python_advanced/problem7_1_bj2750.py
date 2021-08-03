# 문제: 수 정렬하기(백준 2750번)
# 한줄풀이: 어떻게 sort할지, 여기서는 선택정렬을 사용했으나, 다른걸 써도 되고, .sort()가 허용된다면 이게 가장 편할듯

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5


# 1) 선택정렬 알고리즘으로 문제 해결하기
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)

# 2) 파이썬 기본정렬 라이브러리로 문제 해결하기(근데 나같으면 .sort() 쓰라고는 안할듯 테스트니까)

# n = int(input())
# array = list()

# for _ in range(n):
#     array.append(int(input()))

# array.sort()

# for i in array:
#     print(i)