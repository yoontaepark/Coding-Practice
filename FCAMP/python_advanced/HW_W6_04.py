# 과제4.
# 정수로 이루어진 수열 x가 주어졌을 때, x[i-1] < x[i], x[i+1] < x[i]인 x[i]를 피크라고 부른다. 
# 수열 x에 피크가 단 하나 반드시 존재할 때, 이 피크를 찾아 출력하는 O(logN) 알고리즘을 구현하시오. 
# (단, 수열 x의 길이가 N일 때, 반드시 x[0] <= x[1]이며, x[N-1] <= x[N-2]이다.)

# 예시 입력

# x	return
# [-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]	6
# [-1, -1, -1, -1, 0, 1, 20, 19, 17]	20

# https://doromi.tistory.com/90


def solution(x):
    len_x = len(x)
    if len_x < 2:
        return x[0]
    if x[0]>x[1]:
        return x[0]
    if x[-1]>x[-2]:
        return x[len_x -1]
    l = 1
    r = len_x-2
    while l <= r:
        mid = (l+r)//2
        if x[mid] >= x[mid-1] and x[mid]>= x[mid+1]:
            return x[mid]
        if x[mid-1] < x[mid+1]:
            l = mid+1
        else :
            r = mid-1
    return -1


x = [-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]
print(solution(x))

x = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
print(solution(x))
