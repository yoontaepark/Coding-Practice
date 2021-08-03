# 과제3.
# N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 
# 가장 큰 n을 출력하는 알고리즘을 구현하라. (즉, 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라)


def solution(a):

    first_string = a[0]

    if len(first_string) == 0:
        return 0

    for i in range(len(a)-1):
        check_string = a[i+1]

        while len(first_string) > 0:
            if first_string == check_string[:len(first_string)]:
                break
            else:
                first_string = first_string[:len(first_string)-1]
            
        return len(first_string)

# Test code
print(solution(['abcd', 'abceff', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0