# 데이터베이스 및 테이블 생성
# - SQLite 기본 사용법
# - 테이블 생성
# - 데이터 삽입
# - 기본 SQL 사용 예제

# Section 12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3  # 파이썬 깔때 같이 깔림
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatatime: ', nowDatetime)

# sqlite3
print('sqlite3.version: ', sqlite3.version)
print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(<-> Rollback)
conn = sqlite3.connect('C:/Users/YPARK/Desktop/Workspace/python_basic/resource/database.db', isolation_level=None) # isolation은 none이 디폴트

# Cursor
c = conn.cursor()
print('Cursor Type: ', type(c))

# 테이블 생성(Data Type: TEXT, NUMERIC: INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute('INSERT INTO users VALUES(1, "kim", "kim@naver.com", "010-0000-0000", "kim.com", ?)', (nowDatetime,)) # 변수를 넣으려면 ? 로 처리하고 튜플로 넣어야 들어가짐
c.execute('INSERT INTO users (id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)', (2, "Park", "Park@naver.com", "010-1111-1111", "Park.com", nowDatetime)) 


# Many 삽입(튜플, 리스트), 튜플로 다중라인을 만들어놓고, executemany로 해당 변수를 호출하기만 하면 된다. 
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Lee@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

c.executemany('INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)', userList)

# 테이블 데이터 삭제
# conn.execute('DELETE FROM users')
# print('users db deleted: ', conn.execute('DELETE FROM users').rowcount) # .rowcount, 몇줄을 지웠는지 알려줌

# 커밋: isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close() 