# Chapter06_03
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..(/부모) .(현재 디렉토리)


#예제 1
import sub.sub1.module1
import sub.sub2.module2

# 사용

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

#에제 2

from sub.sub1 import module1 #내가 사용하고 싶은 모듈을 패키지에서 찾아간다음
from sub.sub2 import module2 as m2 #alias를 통해서 모듈의 이름을 설정 가능

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

#예제 3
from sub.sub1 import * #비추 다 가져오다보면 메모리 소모가 많다
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()


# 예제 4
import sub.sub3.module3

sub.sub3.module3.mod3_test1()
sub.sub3.module3.mod3_test2()

#예제 5

from sub.sub3 import module3
from sub.sub3 import module3 as m3

module3.mod3_test1()
module3.mod3_test2()


m3.mod3_test1()
m3.mod3_test2()

