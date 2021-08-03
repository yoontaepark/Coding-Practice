# 문제: K번째 수 (백준 11004번)
# 한줄 풀이: 정렬함수를 그냥쓰던지, 아님 퀵/병합/힙 정렬 같은걸 만들기 (2751번이랑 똑같음)


# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

# 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.

# 예제 입력 1 
# 5 2
# 4 1 2 3 5
# 예제 출력 1 
# 2


# # 방법1: 병합정렬함수를 만들어서 그걸 쓴다. 
# def merge_sort(array):
#     # 방어코드
#     if len(array) <= 1:
#         return array
    
#     # 어레이길이가 짝수(ex.4)면 mid는 2니까 인덱스 기준으로 0,1 // 2,3 
#     # 홀수(ex.5)면 mid는 2니까 인덱스 기준으로 0,1 // 2,3,4 
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])
#     i, j ,k = 0, 0, 0

#     # 왼쪽이랑 오른쪽 어레이가 남아있다면 계속 루프
#     while i < len(left) and j < len(right):
#         # 왼쪽이 더 작으면 어레이에 집어넣고 왼쪽 어레이 인덱스를 +1 해준다
#         if left[i] < right[j]:
#             array[k] = left[i]
#             i += 1
#         # 아니면 오른쪽을 어레이에 넣고 오른쪽 어레이 인덱스를 +1 해준다. 
#         else:
#             array[k] = right[j]
#             j += 1 
#         k += 1

#     # 왼쪽 array를 다 썼다면
#     if i == len(left):
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
            
#     # 오른쪽 array를 다 썼다면
#     elif j == len(right):
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#     return array


# n, k = map(int, input().split())
# array = list(map(int, input().split()))

# array = merge_sort(array)

# print(array[k-1])


# 방법2: sorted 함수를 그냥 사용한다. 
n, k = map(int, input().split())
array = list(map(int, input().split()))

array = sorted(array)

print(array[k-1])