# 과제2.
# 오름차순으로 정렬된 N개의 정수를 가진 List가 주어져있을 때, 해당 List에 존재하는 서로 다른 값이 몇 가지인지 알아내는 알고리즘을 구현하라. 
# 알고리즘의 제약사항은 아래와 같다. (알고리즘은 1 <= N <= 10000에서 테스트된다.)

# 추가 메모리 사용은 O(1)으로 제한된다. 따라서 set()와 dict() 등의 자료구조를 사용할 수 없다.
# 알고리즘의 시간복잡도는 O(N) 이하로 제한된다.

def countUniques(a):
    count = 1
    for i in range(1, len(a)):
        if a[i] != a[0]:
            a[0] = a[i]
            count += 1
    return count



# Test code
print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14])) # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) # 2

