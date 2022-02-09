#Chapter04_02
#파이썬 반복문
#For 실습

#코딩의 핵심
#for in <collection>
#    <Loop body>


for v1 in range(10) : #0~9
    print('v1 is', v1 )

for v2 in range(1, 11): #1~10
    print('v2 is', v2)


for v3 in range(1, 11, 2):
    print('v3 is', v3)

print()

#1~1000까지의 합

sum1 = 0
for i in range(1,1001):
    sum1+=i
print(sum)

print('1~1000 sum', sum(range(1, 1001))) #range가 어떤 연속적인 리스트 형태를 만들어주기때문에

print('1~1000 4의 배수의 합', sum(range(4,1001,4)))


#Iteralbes 자료형 반복
#문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
#iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

#예제1
name = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo' ]

for n in name:
    print('You are', n)


word = "Beautiful"

for i in word:
    print('word : ', i)

my_info = {
    "name" : 'Lee',
    "Age" : 33,
    "City" : "Seoul"
}

for k in my_info:
    print('key : ', my_info.get(k)) #get(k), values(),[k]


for v in my_info.values():
    print('value : ', v)

for t in my_info.items():
    print(t)


#예5

name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


#break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]


for num in numbers:
    if num == 34:
        print('Found : 34')
        break
    else:
        print('Not found : ', num)


#continue

lt = ["1,", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type:", v, type(v))
    

# for - else
#파이썬에만 활용되고 있는
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]


for num in numbers:
    if num == 55:
        print("Found : 55")
        break
else:
    print('Not Found :  55') #break문을 만나면 실행되지 않는다.



#구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}' .format(i*j), end='')
    print()


#변환 예제

name2 = 'Aceman'

print('Reversed', reversed(name2)) #형변환을 해줘야 제대로 된 값을 확인 가능
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set : ', set(reversed(name2))) #set은 순서가 없기 때문에 실행할때마다 다른 순서로 값이 나온다.


