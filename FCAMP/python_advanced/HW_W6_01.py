# 과제1.
# 리스트 [1,2,3,...,n] 를 섞는 방법은 총 n! 가지이다. n = 3일 때 3! = 6개의 섞은 결과는 아래와 같은 순서를 가진다고 하자.

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# n과 k가 주어졌을 때, k번째 섞은 결과를 반환하시오. (단, 1 <= n <= 9, 1 <= k <= n!)

# 예시입력

# n	k	return
# 3	3	[2, 1, 3]
# 4	9	[2, 3, 1, 4]

# https://codepractice.tistory.com/59 다시 보자 

def update(the_list, n, result): 
    templist = the_list[n:] 
    templist.sort() 
    the_list = the_list[:n]+templist
    result.append(the_list.copy())
    return the_list

def solution(n, k):
    source = [x for x in range(1, int(n) + 1)] 
    resource = [x for x in range(int(n), 0, -1)] 
    result = [source.copy()] 
    
    while source != resource: 
        for i in range(len(source)-1, 0, -1): 
            if source[i] > source[i-1]: 
                for j in range(i, len(source)): 
                    if source[i-1] > source[j]: 
                        temp = source[i-1]
                        source[i-1] = source[j-1] 
                        source[j-1] = temp 
                        source = update(source, i, result)
                        break 
                    elif j == len(source) - 1:
                        temp = source[i-1] 
                        source[i-1] = source[j] 
                        source[j] = temp 
                        source = update(source, i, result)
                        break
                break

    return result[k-1]

n, k = map(int, input().split())
print(solution(n, k))
