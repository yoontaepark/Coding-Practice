# 문제: 트리 순회(백준 1991번)
# 한줄 풀이: 루트/왼/오에 대한 재귀함수 꼴로 함수를 만든다 / 클래스 변수로 루/왼/오를 하나 만든다. 
# 참고로 중위 순회의 경우 왼쪽 -> 오른쪽 순서대로 출력하면 그게 순서임


# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 예를 들어 위와 같은 이진 트리가 입력되면,

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
# 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

# 예제 입력 1 
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# 예제 출력 1 
# ABDCEFG
# DBAECFG
# DBEGFCA

# Node라는 클래스를 (루트, 좌, 우) 정의 
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    # 루트
    print(node.data, end='')
    # 좌
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    # 우
    if node.right_node != '.':
        pre_order(tree[node.right_node])
            
def in_order(node):
    # 좌
    if node.left_node != '.':
        in_order(tree[node.left_node])
    # 루트
    print(node.data, end='')
    # 우
    if node.right_node != '.':
        in_order(tree[node.right_node])
            
def post_order(node):
    # 좌
    if node.left_node != '.':
        post_order(tree[node.left_node])
    # 우
    if node.right_node != '.':
        post_order(tree[node.right_node])
    # 루트
    print(node.data, end='')



# 첫째 줄에 노드 개수 입력
n = int(input())

# 트리문제는 딕셔너리로 풀생각을 해보자
tree = {}

# 루트, 왼, 오를 반복 입력하면, 클래스에다 값을 넣어둔다. 
for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])


