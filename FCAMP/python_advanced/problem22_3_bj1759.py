# 문제: 암호만들기 (백준 1781번)
# 한줄풀이: 조합 사용, 전체를 정렬시킨다음에 조건에 맞는거만 출력

# 바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 
# 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
# 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
# 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. 
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

# 출력
# 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

# 예제 입력 1 
# 4 6
# a t c i s w

# 예제 출력 1 
# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw

# 방법1: 조합 라이브러리 사용
# from itertools import combinations

# vowels = ('a', 'e', 'i', 'o', 'u')
# l, c = map(int, input().split())

# array = input().split(' ')
# array.sort()

# for password in combinations(array, l):
#     # 모음 개수 세기, 모든 조합에 count 개수가 반영이 되어 있음
#     count = 0
#     for i in password:
#         if i in vowels:
#             count += 1
#     # 자음은 최소 2개있어야 하므로 전체에서 자음 2개 빼도 전체 길이가 모음 길이보다 길어야 함
#     if count >= 1 and count <= l - 2:
#         # 한자씩 떨어져있을거니까 합치기 
#         print(''.join(password))


# 방법2: 조합함수 직접 구현
import copy

result = []
string = []
visited = []

# dfs로 구현
def combination(array, length, index):
    if len(string) == length:
        result.append(copy.deepcopy(string))
        return 
    
    for i in range(index, len(array)):
        if i in visited:
            continue
        string.append(array[i])
        visited.append(i)
        combination(array, length, i+1)
        string.pop()
        visited.pop()

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

array = input().split(' ')
array.sort()

combination(array, l, 0)

for password in result:
    # 모음 개수 세기, 모든 조합에 count 개수가 반영이 되어 있음
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    # 자음은 최소 2개있어야 하므로 전체에서 자음 2개 빼도 전체 길이가 모음 길이보다 길어야 함
    if count >= 1 and count <= l - 2:
        # 한자씩 떨어져있을거니까 합치기 
        print(''.join(password))