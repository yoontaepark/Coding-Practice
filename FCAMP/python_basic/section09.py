# 파일 Read, Write
# - Open 함수
# - 파일 모드의 이해
# - 파일 읽기 실습
# - 파일 쓰기 실습

# Section 09
# 파일 읽기, 쓰기
# 읽기 모드: r, 쓰기 모드(기존 파일 삭제됨): w, 추가 모드(파일 생성 또는 추가): a
# .. : 상대경로, . : 절대경로
# 기타: http://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1: .read() 를 쓰면 끝까지 읽어온다. 
f = open('./resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환해야함!!(open 했다면 중요)
f.close()


print('---------------------------------------------')
print('---------------------------------------------')

# 예제2: with를 쓰면 close 안써도 자동으로 반환이 됨
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))


print('---------------------------------------------')
print('---------------------------------------------')

# 예제3: .strip 함수를 쓰면 양쪽 공백(및 줄바꿈)이 제거됨, 한줄씩 반복문으로 출력한다고 보면 된다. 
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) 


print('---------------------------------------------')
print('---------------------------------------------')

# 예제4: .read()를 다시 쓰면 내용이 없다. 끝까지 읽었기 때문
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read() # 한번 읽었기 때문에 여기엔 내용이 없다
    print('>', content)


print('---------------------------------------------')
print('---------------------------------------------')

# 예제5: readline으로 한줄씩 저장이 가능하고, 반복문으로 뽑을수도 있다. // 처음에 라인 정의는 해야함
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='#####') # '#####' 가 다음줄에 출력되는 이유는, line 찍고, /n 찍은다음에 ##### 이 찍히기 때문
        line = f.readline()

print('---------------------------------------------')
print('---------------------------------------------')

# 예제6: readlines라는게 있음, 전체 목록을 리스트로 저장함
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ****** ')

print('---------------------------------------------')
print('---------------------------------------------')

# 예제7: 저장되어 있는 숫자들을 리스트로 저장 및 출력하기(.txt는 숫자여도 문자여서)
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line)) # int 변환해줘야 됨, 문자형태의 숫자들이기 때문 
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score))) # {:6.3} 은 앞 공백+정수2+소수점3 으로 총 6자리로 출력해라 라는 소리



# 파일 쓰기
# 예제1 : w는 없으면 생성, 있으면 덮어씀 
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman\n')

# 예제2 : a도 없으면 생성, 있으면 추가 
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman\n')

# 예제3: 로또번호 랜덤으로 뽑기
from random import randint  # 랜덤으로 숫자뽑으려고 랜덤함수 패기지 호출

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):    # 0, 1, 2, 3, 4, 5 로 총 6회 반복
        f.write(str(randint(1,50))) # write 함수는 str만 받아서 str로 형변환 해줄 것
        f.write('\n')

# 예제4
# writelines: 리스트 -> 파일로 저장하는 기능
with open('./resource/text3.txt', 'w') as f:
    list1 = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list1)

# 예제5: print문 활용, 뒤에 file= 넣으면 콘솔창에 출력이 안되고 파일에 프린트문을 생성해줌
with open('./resource/text4.txt', 'w') as f:
    print('Test Contest1', file=f)
    print('Test Contest2', file=f)