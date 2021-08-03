# 과제2. 
# 여러 개의 구간이 리스트 intervals로 주어졌을 때, 겹치는 구간을 모두 병합하여 출력하시오.

# 입력 예시1

# 입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 출력: [[1,6],[8,10],[15,18]]
# 설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.
# 입력 예시 2

# 입력: intervals = [[1,4],[4,5]]
# 출력: [[1,5]]
# 설명: 구간 [1,4]와 [4,5]는 겹치는 것으로 간주한다.

def solution(intervals):
    answer = []
    for arr in sorted(intervals, key=lambda x: x[0]):
        if answer and arr[0] <= answer[-1][1]:
            answer[-1][1] = max(answer[-1][1], arr[1])
        else:
            answer.append(arr)
    
    return answer


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution(intervals))

intervals = [[1,4],[4,5]]
print(solution(intervals))

