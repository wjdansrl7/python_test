#Chapter08_01
# 파이썬 내장(Built_in) 함수
# str() int() tuple() 형변환 이미 학습

#절대값
print(abs(-8))

#all, any: iterable 요소 검사함(참, 거짓)

print(all([1,2,3])) # and 하나라도 0이 있거나 빈 문자열 모두가 true여야 true
print(any([1,2,0])) #or

#chr : 아스키 -> 문자, ord : 문자-> 아스키

print(chr(67))
print(ord('C'))

# enumerate :  인덱스 +  Iterable 객체 생성

for i, v in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, v)


# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: abs(x)>2, [1, -3, 2, 0 ,-5 , 6])))
# 이럴때 람다함수가 빛을 발하는데 한 번 쓰고 말 함수일 경우

# id : 객체의 주소값(레퍼런스) 변환

print(id(int(5)))
print(id(4))


# Len : 요소의 길이 반환
print(len('abddefg'))
print(len([1,2,2,3,3,44]))

#max, min :  최대값, 최소값

print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study')) #공백이 가장 작은 값

#오늘 제일 중요한 것 : enumerate, filter , map

#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출

def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3, 2, 0, -5, 6]))) #함수에 결과값들을 추출후 보여줌
print(list(map(lambda x: abs(x),[1,-3, 2, 0, -5, 6]))) #함수에 결과값들을 추출후 보여줌

#pow : 제곱값 반환
print(pow(2,10))

#range : 반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

#round : 반올림

print(round(6.5789, 2))
print(round(5.6))

# list, tuple, set, dict 중요
# sorted : 반복가능한 객체(Iterable) 정렬 후 반환

print(sorted([6,7,4,3,2,21,]))

a = sorted([56,6,4,3,2,1,6,6])
print(a)

print(sorted(['p', 'y', 't','h', 'o', 'n']))


# sum : 반복가능한 객체(Iterable) 합 반환

print(sum([6,7,8,6,5,4]))
print(sum(range(1,101)))

# type : 자료형

print(type(3))
print(type({}))
print(type(()))
print(type([]))

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환

print(list(zip([10,20,30],[30,40,50])))
print(type(zip([10,20,30],[40,50]))) #짝이 없으면 반환하지 않는다.
# 튜플 형태를 list로 감싼거다.

 









