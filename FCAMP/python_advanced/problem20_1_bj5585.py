# 문제: 거스름돈 (백준 5585번)
# 한줄풀이: 탐욕 알고리즘, 가장 큰 화폐 단위 순서대로 잔돈을 거슬러주면 된다. 

changes = 1000 - int(input())
count = 0

# 큰 단위부터 한번씩 수행하면서 나눠본다. i보다 작으면 변화없음
for i in [500, 100, 50, 10, 5, 1]:
    count += changes // i
    changes %= i

print(count)