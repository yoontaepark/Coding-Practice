# Excel, CSV 처리
# - CSV 읽기
# - CSV 쓰기
# - XSL, XLSX 읽기
# - 패키지 설치

# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV: MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f) # csv 파일을 읽어오는 함수, 리스트 형태로 읽어옴, 구분자는 ,가 기본값
    next(reader) # Header 스킵, 반복하면 다음행 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

print('---------------------------------------')
print('---------------------------------------')

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # csv 파일을 읽어오는 함수, 지정되어 있는 구분자 없애기
    next(reader) # Header 스킵, 반복하면 다음행 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


print('---------------------------------------')
print('---------------------------------------')

# 예제3: Dict으로 변환

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        print(c) # dic 형태로 정의되어 있으니 키와 벨류를 한꺼번에 뽑을 수 있다. 
        for k,v in c.items():
            print(k,v)
        print('--------------')


print('---------------------------------------')
print('---------------------------------------')

# 예제4: Dict -> csv로 변환, 한줄씩 반복해서 변환
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f: # newline은 기본적으로 한줄씩 있는데 없애는 기능
    wt = csv.writer(f) # 이거도 w 를 하기 위해 불러오는 함수다 라고 생각하기

    for v in w:
        wt.writerow(v) # 여기에도 리스트 하나 끝날때마다 엔터있음


print('---------------------------------------')
print('---------------------------------------')

# 예제5: ict -> csv로 변환, 전체를 변환
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html 을 참고
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# read_excel 뒤에다가 추가 옵션을 넣을수 있다 .
# sheet_name = '시트명' 또는 숫자로 시트선택 // header=숫자, skiprows=숫자
xlsx = pd.read_excel('./resource/sample.xlsx', sheet_name=0, header=0, skiprows=0) # 전부 default값이며 안써도 됨

# 상위 데이터 확인
print(xlsx.head()) # 첫 5줄의 데이터를 보여줌
print()

# 데이터 확인
print(xlsx.tail()) # 마지막 5줄의 데이터를 보여줌 

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
