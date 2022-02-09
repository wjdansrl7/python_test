#자료구조에서 중요

#리스트 자료형(순서o, 중복o, 수정o, 삭제o)

#선언

a=[]
b=list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.13434]


#인덱싱
print('>>>>')
print('d-', type(d), d)
print('d - ', d[1])
print('d -', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', d[-1][1])
print('e - ', list(e[-1][1])) #문자열은 시퀀스라서

#슬라이싱
print('>>>>')
print('d - ', d[2:])
print('e - ', e[-1][1:3])

#리스트 연산

print('>>>>')
print(c+d) #리스트 + 리스트 = 리스트
print(c*3)
print("'Test' + c[0]", 'Test' + str(c[0]))

#값 비교

print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

#Identitiy(id)

temp = c
print(temp, c)

print(id(c))
print(id(temp))

#리스트 수정, 삭제

print('>>>>>>>>>')
c[0] = 4
print('c - ', c)

c[1:2] = ['a', 'b', 'c'] # 리스트와의 연산이어서 리스트로 [['a','b','c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']  #리스트안에 중첩
print('c - ', c)

c[1:3]=[]
print('c - ', c)
 
del c[2] #삭제
print('c - ', c)

 #리스트 함수

a = [5,2,3,1,4]

print('a - ', a)

a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)
#del a[8789]
a.remove(10)
print('a - ', a)

print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) #내가 찾는 값이 몇개인가?

ex = [8, 9]

a.extend(ex)

print('a - ', a)


#삭제 : remove, pop, del

#반복문 활용

while a:
    data = a.pop()
    print(data)








