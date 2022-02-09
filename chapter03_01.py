#파이선 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 볼린
str : 문자열
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합  
dict : 사전
"""

str1 = "Python"
str2 = "Anaconda"
list = [str1,str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}

tuple = (7,8,9) #가로 안쳐도됨
set = {3,5,7}

"""
abs(x) : 절대값
pow(x,y) x ** y -> 2 ** 3
"""

i1 = 3
i2 = 4
f1 = 3.23213
f2 = 0.9999

print("i1+i2 : ", i1+i2)

#형 변환 연습

a=3.
b=5
c=.7
d=12.6

print(type(a),type(b),type(c),type(d))

print(float(b))

print(int(d))

# True : 1 False : 0

print(complex(b))

print(complex('3')) # 문자형 -> 숫자형

#수치 연산 함수
print(abs(-7))
x,y = divmod(100,8)

print(x,y)

print(pow(5,3))


#외부 모듈
import math

print(math.pi)


print(math.ceil(5.1)) #x 이상의 수 중에서 가장 작은 정수







