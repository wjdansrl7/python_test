import sys


print(sys)

print(sys.path)

print(type(sys.path)) # append, insert, index 리스트일때에는

# 모듈 경로 삽입
#sys.path.append('/users/moongi/Documents/repos/math')
 
print(sys.path)

#import test_module


#print(test_module.power(10,3))


import chapter06_02 #영구적으로 사용할꺼면 환경변수에 따로 경로를 저장해야한다.

print(chapter06_02.add(10, 10))





 