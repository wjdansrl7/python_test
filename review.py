# 파이썬 내장함수(Built_in)



print(abs(-8))

#all, any : iterable 요소 검사함(참 거짓)

print(all([1,2,3]))

print(all([1,2,0])) # and

print(any([1,2,0])) # or

# chr : 아스키 -> 문자 , ord : 문자 -> 아스키

print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + iterable 객체 생성

for i, v in enumerate(['abc','def','ghi']):
    print(i+1, v)

# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos,[1,-2,3,-6, 7])))


print(list(filter(lambda x: abs(x)>2,[1,3,-5,7,-9, 4])))

#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출

def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,4,-8,7])))
#함수에 결과값들을 추출후 보여줌

#pow : 제곱값 반환
print(pow(10,3))

#range:반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))

print(list(range(1,10, 3)))

print(list(range(3,20,3)))



set = {1,5,3,2}

print(sorted(set))

li = [5,3,8,4]
tu = (4,8,7,2)

print(sorted(li))
print(sorted(tu))


print(sum([1,3,4,5]))


print(list(zip([1,2,3],[4,5,6])))

#튜플 형태를 리스트로 감쌌다.


import sys
print(sys.argv)



# pickle : 객체 파일 쓰기
import pickle

f = open('tex.obj', 'wb')
obj = {1: 'python', 2: 'study', 3:'basic'}
pickle.dump(obj, f)
f.close()

f = open('tex.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
#mkdir, rmdir(비어있으면 삭제), remove

#예제 6

import os
print(os.environ)

print(os.getcwd()) #현재경로

import time

print(time.time())

print(time.localtime(time.time()))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


import random

# for i in range(5):
#     print(i)
#     time.sleep(1)

print(random.randint(1,45))
print(random.randrange(1,45))

d = [1,2,3,4,5]

random.shuffle(d)
print(d)


