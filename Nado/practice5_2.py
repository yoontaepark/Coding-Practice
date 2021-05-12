## continue, break
# continue: 계속해서 다음 반복문을 진행(반목문 위로 올라감)
# break: 반복문을 종료하고 끝내기 

absent = [2,5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11):
    if student in absent:
        print("오늘 {0}번 결석이니? 다음번호".format(student))
        continue  # 다음 반복문을 진행, 즉 위의 for문을 다시 시작
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로".format(student))
        break # 반복문 자체를 빠져나옴
    else:
        print("{0}, 책을 읽어보렴".format(student))

print("수업이 종료되었다.")

## 한줄 for 문
# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 → 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]  # 여기에서 i는 특별한 의미는 없고 그냥 변수만 맞춰주면 됨
print(students)

# 학생 이름을 길이로 변환
students2 = ["Amy", "Bruno", "Chris"] 
students2 = [len(i) for i in students2] #len 함수를 쓰고 구도는 동일
print(students2)

# 학생 이름을 대문자로 변환
students3 = ["Amy", "Bruno", "Chris"] 
students3 = [i.upper() for i in students3] #.upper를 쓰고 구도는 동일
print(students3)
