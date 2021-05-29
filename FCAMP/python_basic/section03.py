# 파이썬 가상환경 명령어 기초
# 가상환경 생성 : -m venv python_basic 
# 가상환경 실행/해제 -> (윈도우: Script, 맥: Bin) 폴더
# 패키지 설치 및 삭제: pip install simplejson
# 패키지 리스트 출력: pip list
# 패키지 검색: pip search simple*



# Section3
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1':95, '4': 77, '3':65, '5':100, '2':88 }

#simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))

