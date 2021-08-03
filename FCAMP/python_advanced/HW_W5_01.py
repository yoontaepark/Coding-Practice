# 과제1.
# 이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다. 
# 이진탐색을 이용하여 인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 target을 찾으면 True를 반환하고, 
# target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.

def searchMatrix(matrix, target):
    if len(matrix) == 1 and target == matrix[0]:
        return True
    if len(matrix) == 1 and target != matrix[0]:
        return False
    if len(matrix) == 0:
        return False
    
    medium = len(matrix) // 2
    if target == matrix[medium]:
        return True
    else:
        if target > matrix[medium]:
            return searchMatrix(matrix[medium+1:], target)
        else:
            return searchMatrix(matrix[:medium], target)


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3
new_matrix = sum(matrix, []) # 2차원 배열을 1차원으로 풀기

print(searchMatrix(new_matrix, target))