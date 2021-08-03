# 과제4.
# 마을에 1부터 N의 고유 번호를 가진 사람들이 있다. 소문으로는 마을 사람 중에 마을 판사가 있다고 한다. 마을 판사가 실제로 존재한다면,

# 마을 판사는 아무도 믿지 않는다.
# 다른 모든 사람들은 마을 판사를 믿는다.
# 마을 판사가 있다면 오직 한명 뿐이다.
# 리스트 trust가 주어졌을 때, trust[i] = [a, b]는 고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.

# 마을 판사가 존재한다면 마을 판사의 고유 번호를, 존재하지 않는다면 -1을 출력하는 프로그램을 작성하시오.

# (단, a가 b를 믿고 b가 c를 믿는다고 할 때, a가 c를 믿는다는 의미는 아니다.)

# 예시입력


# N	trust	                        출력
# 2	[[1,2]]	                        2
# 3	[[1,3],[2,3]]	                3
# 3	[[1,3],[2,3],[3,1]]	            -1
# 3	[[1,2],[2,3]]	                -1
# 4	[[1,3],[1,4],[2,3],[2,4],[4,3]]	3


# 배열을 두개 만들기 (내가 타인을 믿는 횟수, 타인이 나를 믿는 횟수)
# 리스트가 한번씩 돌때마다, 첫번째 배열과 두번째 배열을 각각 업데이트해서, 
# 최종적으로 [0, N-1] 이 있는지 확인하고, 있다면 해당 배열의 인덱스를 +1해서 출력 (없으면 -1)
def solution(N, trust):
    
    # 사람이 한명이라면 판사인지 아닌지 알 수 없음
    if N == 1:
        return "Can't decide"
    
    # 초기화
    people = [0 for _ in range(N)]
    trusted = [0 for _ in range(N)]

    # trust 리스트를 돌리면서, 각 배열의 인덱스를 찾아가서 값을 1씩 더해줌 
    for i in range(len(trust)):
        people[trust[i][0]-1] += 1
        trusted[trust[i][1]-1] += 1
    
    # 다 돌고나서 0,N-1을 찾기, 있으면 해당 배열 인덱스번호 + 1
    if N-1 in trusted and 0 in people and people.index(0) == trusted.index(N-1):
        return trusted.index(N-1)+1
    
    return -1

N = 2
trust = [[1,2]]	
print(solution(N, trust))


N = 3
trust = [[1,3],[2,3]]	
print(solution(N, trust))

N = 3
trust = [[1,3],[2,3],[3,1]]	 
print(solution(N, trust))

N = 3
trust = [[1,2],[2,3]]	
print(solution(N, trust))

N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]	
print(solution(N, trust))

