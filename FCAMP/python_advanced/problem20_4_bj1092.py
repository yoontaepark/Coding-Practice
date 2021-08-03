# 문제: 배 (백준 1092번)
# 한줄풀이: 박스를 내림차순으로 정렬(무거운거부터), 매 분마다 모든 크레인에 대해 옮길 수 있는 박스를 선택 

# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 
# 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 
# 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

# 예제 입력 1 
# 3
# 6 8 9
# 5
# 2 5 2 4 7
# 예제 출력 1 
# 2

import sys
n = int(input())
cranes = list(map(int, input().split()))


m = int(input())
boxes = list(map(int, input().split()))

# 크레인보다 박스가 더 크면 애시당초 성립이 안됨
if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

# 각 크레인이 옮길 박스번호 (각 인덱스마다 1번 / 2번 / 3번 크레인이고, 0번부터 박스번호는 시작해서 올라감)
positions = [0] * n

# 각 박스를 옮겼는지 여부
checked = [False] * m

# 둘다 내림차순으로 소트(큰거부터)
cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0

while True:
    # 박스를 다 옮겼으면 while문 종료
    if count == len(boxes):
        break
    
    # 모든 크레인에 대해서
    for i in range(n):
        # 박스번호마다 체크, 박스번호가 박스 총개수보다 많아지면 당연히 while문 종료하지만, 사실상 다 돌리라는 소리임(위에 if문에서 마무리됨)
        while positions[i] < len(boxes):
            # 박스를 안 옮겼으면서, 크레인이 박스보다 크면 옮김
            # count 는 박스 개수를 센다라고 이해, checked는 옮겼다 체크, positions[i]는 해당 크레인 기준으로 0번 박스는 제꼈으니 1번박스로 한칸 올려준다
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break

            # 바로위의 if문에 걸리지 않았더라도, 첫박스는 검사한거니까 다음박스로 한칸 올려준다. 
            positions[i] += 1

    # while문 한번당 1분씩 증가       
    result += 1

print(result)


