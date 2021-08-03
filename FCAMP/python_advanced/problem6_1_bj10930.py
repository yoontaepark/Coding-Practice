# 문제: SHA-256 (백준 10930)
# 한줄풀이: SHA-256, 해시, 구현. 그냥 해시 라이브러리를 통해 SHA-256 해시를 구할 수 있느냐를 물어보는 문제

# 문제
# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

# 출력
# 첫째 줄에 S의 SHA-256 해시값을 출력한다.

# 예제 입력 1 
# Baekjoon
# 예제 출력 1 
# 9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857

import hashlib

input_data = input()

# 문자열을 바이트 객체화함
encoded_data = input_data.encode()

# 바이드객체를 해쉬로 바꾸고, 이를 문자열로 출력
result = hashlib.sha256(encoded_data).hexdigest()
print(result)

