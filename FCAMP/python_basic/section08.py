# 모듈, 패키지
# - 패키지 설정
# - 모듈 사용 및 Alias 설정
# - 패키지 사용 장점

# Section 08 
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print('ex1: ', Fibonacci.fib(300)) # none 
print('ex1: ', Fibonacci.fib2(400))
print('ex1: ', Fibonacci().title)


# 사용2(클래스)
from pkg.fibonacci import * # 해당 파일에 있는 모든 클래스를 import, 데이터 사용량이 많아서 잘 안씀

Fibonacci.fib(500)
print('ex2: ', Fibonacci.fib2(600))
print('ex2: ', Fibonacci().title)


# 사용3(클래스) : 이건 권장
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)
print('ex3: ', fb.fib2(1100))
print('ex3: ', fb().title)


# 사용4(함수) : 함수만 있으면 from 안쓰고 바로 import 가능

import pkg.calculations as c  # 이 경우 개별의 함수를 끌어오는게 안되고 전체를 끌어오는거만 됨

print('ex4: ', c.add(10, 100))
print('ex4: ', c.mul(10, 100))

# 사용5(함수): 함수 중에서도 개별 함수만 끌고 오고 싶으면 그냥 from을 쓰자! 
from pkg.calculations import div as d
print('ex5: ', int(d(100,10)))


# 사용6(함수)
import pkg.prints as p 

p.prt1()
p.prt2()

# 참고, builtins 패키지는 이미 다 깔려있어서 선언을 안해도 되는 것임
import builtins
print(dir(builtins))