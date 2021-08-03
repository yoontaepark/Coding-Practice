# 문제: 소트 인사이드(백준 1427번)
# 한줄풀이: 9->0 까지 루프돌면서 각 자리수가 해당 숫자와 일치하면 출력한다. 

# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
# 첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# 예제 입력 1 
# 2143
# 예제 출력 1 
# 4321


array = input()

# 9 -> 0 까지 비교를 위한 수 반복
for i in range(9, -1, -1):
    # 놀랍게도 4자리수 이러면 이걸 한자리씩 쪼개서 루프가 돈다
    for j in array:
        if int(j) == i:
            print(i, end='') # end에 빈 문자열을 넣으면 다음번 출력이 바로 뒤에 오게 됨