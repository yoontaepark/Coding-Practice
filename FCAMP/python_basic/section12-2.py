# 다양한 테이블 조회
# - SQLite 기본 사용법
# - Selete
# - Where
# - Tuple, Dictionary Mapping


# Section 12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Users/YPARK/Desktop/Workspace/python_basic/resource/database.db') # 본인 DB 경로

# 커서 바인딩
c = conn.cursor()

## 데이터 조회(전체)
c.execute('SELECT * FROM users')  # 실행을 한 것이라고 보면 됨. 출력은 아래처럼 print문으로 찍는다. 

# 조회 시 커서 위치가 변경됨
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택(ex.3개)
# print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())

# print('All -> \n', c.fetchall()) # 데이터를 다 호출되었으므로 빈 리스트가 나온다.

print()

# 순회1, 변수선언하고 다시 돌리니까 좀 코드가 길다
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회2, 많이 쓰는 방법으로 변수없이 바로 fetchall함수를 순회
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회3, 그냥 아예 execute까지 합쳐서 순회하기, 코드가 좀 복잡해서 잘 안씀
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrive3 > ', row)


# WHERE Retrieve1 (총 6가지 조회 방법), 단일 + 튜플
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 바로윗줄에서 3번을 썼기 때문에, 3번은 조회가 안됨, 빈 리스트가 출력됨

# WHERE Retrieve2 , 단일 + % 형태
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall()) # 마찬가지로 데이터 없음

# WHERE Retrieve3, 단일 + 딕셔너리
c.execute('SELECT * FROM users WHERE id=:Id', {"Id":5})
print('param3', c.fetchone())
print('param3', c.fetchall())

# WHERE Retrieve4, 다중 + 튜플
param4 = (3,5,)
c.execute('SELECT * FROM users WHERE id IN (?,?)', param4)
print('param4', c.fetchall())

# WHERE Retrieve5, 다중 + %
c.execute('SELECT * FROM users WHERE id IN ("%d","%d")' % (3,4))
print('param5', c.fetchall())

# WHERE Retrieve6, 다중 + 딕셔너리
c.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2', {"id1":2, "id2":5})
print('param6', c.fetchall())


# Dump 출력, SQL에서 실행할 수 있는 명령문을 출력함
with conn:
    with open('C:/Users/YPARK/Desktop/Workspace/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.cloase(), conn.close()는 기 실행됨(with 문이므로)
 