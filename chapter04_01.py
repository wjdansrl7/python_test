#Chapter04-01
#파이선 제어문
#IF 실습

#기본 형식
print(type(True)) #0이 아닌 수, "abc", (1, 2,3, ..)
print(type(False))


#예1

if True:
    print("Good")


if False:
    print('Bad')


# 예2
if False:
    print('Bad')
else:
    print('Good')

city = ""
if city:
    print('you are in', city)
else:
    print('plz enter your city')

#산술 > 관계 > 논리

#다중조건문

num =90

if num>=90:
    print('Grade : A')
elif num >=80:
    print('Grade : B')
else:
    print("과락")


#in, not in

q = [10, 20, 30]
w = [70, 80, 90, 100]
e = {"name" : "Lee", "city" : "Seoul", "grade" : "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())





