# 문제: 수 정렬하기2 (백준 2751번)
# 한줄 풀이: 정렬함수를 그냥쓰던지, 아님 퀵/병합/힙 정렬 같은걸 만들기 (여기에선 병합정렬을 만들어볼 에정)


# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 4
# 3
# 2
# 1

# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5


# 방법1: 병합정렬함수를 만들어서 그걸 쓴다. 
def merge_sort(array):
    # 방어코드
    if len(array) <= 1:
        return array
    
    # 어레이길이가 짝수(ex.4)면 mid는 2니까 인덱스 기준으로 0,1 // 2,3 
    # 홀수(ex.5)면 mid는 2니까 인덱스 기준으로 0,1 // 2,3,4 
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j ,k = 0, 0, 0

    # 왼쪽이랑 오른쪽 어레이가 남아있다면 계속 루프
    while i < len(left) and j < len(right):
        # 왼쪽이 더 작으면 어레이에 집어넣고 왼쪽 어레이 인덱스를 +1 해준다
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        # 아니면 오른쪽을 어레이에 넣고 오른쪽 어레이 인덱스를 +1 해준다. 
        else:
            array[k] = right[j]
            j += 1 
        k += 1

    # 왼쪽 array를 다 썼다면
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            
    # 오른쪽 array를 다 썼다면
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
    return array


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)


# 방법2: sorted 함수를 그냥 사용한다. 
# n = int(input())
# array = []

# for _ in range(n):
#     array.append(int(input()))

# array = sorted(array)

# for data in array:
#     print(data)