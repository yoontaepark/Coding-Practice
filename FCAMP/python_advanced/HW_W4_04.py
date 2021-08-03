# 과제4.
# 자연수 중, 각 자리수를 제곱한 것을 더하는 과정을 반복했을 때 1으로 끝나는 수를 '행복한 수'라고 한다. 
# '행복한 수'가 아닌 경우 이 과정이 1에 도달하지 못하고 같은 수열이 반복되는 무한 루프에 빠지게 된다. 자연수를 입력받았을 때 '행복한 수'인지 판별하는 알고리즘을 작성하라.

# '행복한 수'를 찾는 과정의 예

#   19이 행복한 수인지 확인하는 과정
#   1^2 + 9^2 = 82
#   8^2 + 2^2 = 68
#   6^2 + 8^2 = 100
#   1^2 + 0^2 + 0^2 = 1 --> True

def solution(n):

    try: 
        if n == 1:
            return True

        sum = 0
        while(n > 0):
            next_digit = n % 10
            n = n // 10
            sum += next_digit ** 2

        return(solution(sum))
    
    except RecursionError:
        return False

 
# Test code
print(solution(19)) # True
print(solution(61)) # False
