# 타이밍 게임 기본 완성
# - 단어 리스트 로드
# - 총 게임 시간 측정
# - 정답 개수 체크

# Section 13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = []      # 영어 단어 리스트(1000개 로드)

n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('C:/Users/YPARK/Desktop/Workspace/python_basic/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words)    # 단어 리스트 확인

input('Ready? Press Enter Key!') # Enter Game Start!

start = time.time()

while n <= 5:
    random.shuffle(words) # 섞어주는 함수
    q = random.choice(words) # 선택하는 함수

    print()

    print('*Question # {}'.format(n))
    print(q) # 문제 출력

    x = input() # 타이핑 입력, 이런식으로 변수로 선언을 하면 입력하는데로 출력이 된다. 문자열 형태로 들어옴

    print()

    if str(q).strip() == str(x).strip():
        print('Pass!')
        cor_cnt += 1
    else:
        print('Wrong!')

    n += 1 # 다음 문제 전환

end = time.time() # End time
et = end - start    # 총 게임시간
et = format(et, '.3f') # 소수점 셋째 자리 출력(시간)

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 수행 시간 출력
print('게임 시간: ', et, '초, 정답 개수: {}'.format(cor_cnt))



# 시작 지점(여기에서만 실행했을 때 돌려라 라는 뜻)
if __name__ == '__main__':
    pass