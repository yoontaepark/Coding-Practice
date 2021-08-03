# 문제: 0만들기 (백준 7490번)
# 한줄 풀이: ///

# 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.
# 그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.
# N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.

# 입력
# 첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).
# 각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).

# 출력
# 각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.

# 예제 입력 1 
# 2

# 3
# 7

# 예제 출력 1 
# 1+2-3
# 1+2-3+4-5-6+7
# 1+2-3-4+5+6-7
# 1-2 3+4+5+6+7
# 1-2 3-4 5+6 7
# 1-2+3+4-5+6-7
# 1-2-3-4-5+6+7

import copy

# 재귀함수 선언
def recursive(array, n):
    # 어레이가 특정 숫자길이에 도달할때
    if len(array) == n:
        # 여태 array에 만들었던걸 독립적인 변수를 만들어서 복사뜨고 종료
        operators_list.append(copy.deepcopy(array)) 
        return 

    # 공백, +, - 각각에 대해 재귀로 넣으면 위의 if문에 걸려서 operators로 감, 그리고 없었던거처럼 pop으로 없앰
    array.append(' ')
    recursive(array, n)
    array.pop()

    # 위의 설명과 동일하게 이제 + 부터 시작
    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()


# 몇회할건지
test_case = int(input())

# 각 케이스마다
for _ in range(test_case):

    # 연산자 리스트 초기화
    operators_list = []

    # 연산자는 자연수 N보다 1개 적은 순서쌍이 됨
    n = int(input())
    # 함수를 호출하는데 N-1이 들어감
    recursive([], n-1)

    # 함수와 별개로, 1부터 선언한 자연수 N까지 숫자 나래비
    integers = [i for i in range(1, n+1)]

    # 연산자 쌍들에 대해서
    for operators in operators_list:
        # STRING 만들건데
        string =''
        # 0번 인덱스부터 n-2번 인덱스까지 (즉, 1부터 n-1까지)
        for i in range(n-1):
            # 정수는 스트링으로, 연산자는 이미 스트링, 두개를 더하고
            string += str(integers[i]) + operators[i]
        # n번째 정수도 스트링으로 변환해서 더하기
        string += str(integers[-1])

        # 연산자가 비어있다면 사이 숫자들은 걍 붙이라고 했으니 공백을 없애고, eval함수를 통해 str 연산을 해보면 된다.  
        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()