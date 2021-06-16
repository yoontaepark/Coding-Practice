# 데이터 수정 및 삭제
# - UPDATE
# - DELETE
# - DB 사용 권장 이유


# Section 12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('C:/Users/YPARK/Desktop/Workspace/python_basic/resource/database.db')

# Cursor 연결, 말그대로 마우스 커서 위치를 처음으로 땡겨오기
c = conn.cursor()

# # 데이터 수정1, 튜플 형태
# c.execute('UPDATE users SET username = ? WHERE id = ?', ('niceman', 2))
# conn.commit() # 커밋을 해야 바뀐다. 

# # 데이터 수정2, 딕셔너리 형태
# c.execute('UPDATE users SET username = :name WHERE id = :id', {'name': 'goodman', 'id':5})

# # 데이터 수정3, % 형태
# c.execute('UPDATE users SET username = "%s" WHERE id = "%s"' % ('badboy', 3))

# 중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)


# Row Delete1
c.execute('DELETE FROM users WHERE id = ?', (2,))

# Row Delete2
c.execute('DELETE FROM users WHERE id = :id', {"id" : 5})

# Row Delete3
c.execute('DELETE FROM users WHERE id = "%s"' % 4)

print()

# 중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

# 테이블 전체 데이터 삭제
print('users db deleted: ', conn.execute('DELETE FROM users').rowcount, ' rows')

# 커밋
conn.commit()

# 접속해제
conn.close()







