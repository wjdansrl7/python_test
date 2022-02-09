# 집합(Set)의 특징
# 집합(Set) 자료형(순서x, 중복 x)

a = set()

print(type(a))
b = set([1,2,3,4])
c = set([1,4,5,6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} #dict형태여도 안에 키값이 없으면 set으로 설정
f = {42, 'foo', (1, 2, 3), 3.14545}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)


#튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)

#리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l -', l)
print('l2 - ', l2)


#집합 자료형 활용

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4,5,6,7,8,9])

print('S1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))

print('s1 | s2', s1.union(s2))
print('s1 | s2', s1 | s2)

print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))

#중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2)) #False 교집합 있다

#부분 집합 확인
print('subset :',s1.issubset(s2))
print('superset : ',s1.issuperset(s2))

#추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1 -', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7) #없는 값 입력시 예외 발생

s1.discard(3) 
print('s1 - ', s1)
s1.discard(7) #없는 값 입력시 예외 발생 x

s1.clear()
print('s1 - ', s1)

a = [1,2,3]
a.clear()
print(a)





