# 과제2.
# 두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

# 문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
# 가능한 C 중에 가장 긴 문자열을 C로 한다.
# 위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
# 이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.

# 예시입력1

# A = 'ababcde'
# B = 'ababcde'
# 출력: 'ababcde'
# 예시입력2

# A = 'ababababab'
# B = 'abab'
# 출력: 'ab'
# 예시입력3

# A = 'abababab'
# B = 'abab'
# 출력: 'abab'
# 예시입력3

# A = 'fast'
# B = 'campus'
# 출력: ''

def gcdString(A, B):

    l1, l2 = len(A), len(B)
    res = "''"

    for i in range(min(l1,l2), 0, -1):
        if l1 % i or l2 % i: # 둘다 나누어 떨어지면 아래를 수행, 둘 중 하나라도 나누어 떨어지면 루프로 다시 올림
            continue

        t1, t2 = l1 // i, l2 // i
        gcd = A[:i]
        print(i)
        print(gcd)
        rebuild_A = gcd * t1
        print(rebuild_A)
        rebuild_B = gcd * t2
        print(rebuild_B)

        if rebuild_A == A and rebuild_B == B:
            res = gcd
            break

    return res

  


A = 'ababcde'
B = 'ababcde'


print(gcdString(A, B))
print()

A = 'ababababab'
B = 'abab'
print(gcdString(A, B))
print()

A = 'abababab'
B = 'abab'
print(gcdString(A, B))
print()

A = 'fast'
B = 'campus'
print(gcdString(A, B))
print()

