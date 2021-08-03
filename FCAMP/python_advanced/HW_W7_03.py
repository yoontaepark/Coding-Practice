# 과제3.
# 문자열 s1, s2, s3가 주어졌을 때, 문자열 s3가 문자열 s1과 s2를 교차로 배치하여 만들어질 수 있는지 여부를 출력하라.

# 예시 입력1

# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 출력: True
# 예시 입력2

# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 출력: False


def solution(s1, s2, s3):

    # 방어코드: 애초에 길이가 다르면 틀렸음
    if len(s1) + len(s2) != len(s3):
        return False

    def rec(i,j,k):
        # 최종적으로 각 길이를 다썼으면 true가 나옴
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        
        b1, b2 = False, False
        # 아직 길이 미만이면서, i번째 인덱스가 k번째 인덱스와 같을 때 
        if i < len(s1) and s1[i] == s3[k]:
            b1 = rec(i+1, j, k+1)
            
        # 아직 길이 미만이면서, j번째 인덱스가 k번째 인덱스와 같을 때 
        if j < len(s2) and s2[j] == s3[k]:
            b2 = rec(i, j+1, k+1)

        # 최종적으로 나온 b1 혹은 b2의 값이 true면 최종적으로 true가 됨
        return b1 or b2       

    # 재귀함수를 돌리는데 (0,0,0) 부터 시작한다. 
    return rec(0,0,0)

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(solution(s1, s2, s3))


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(solution(s1, s2, s3))



