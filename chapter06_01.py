#Chapter06_01
#파이썬 클래스
#OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해

# 예제 1

class Dog:  #Object 상속
    pass
    # 클래스 속성
    species = "firstdog" # 클래스 변수

    #초기화//인스턴스속성 #c++에서 생성자와 비슷
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스는 틀, 인스턴스는 클래스를 가지고  찍어대는 객체
#인스턴스가 클래스에 포함

#클래스 정보
print(Dog)


#인스턴스화

a = Dog('mikey', 2)
b = Dog('bagr', 4)
c = Dog('mikey', 2)

#비교

print(a==b) #False
print(id(a), id(b))
print(a==c) # 인스턴스화 시킨 것은 서로 다르다.


# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
#클래스 변수 : 직접 접근 가능
#인스턴스 변수 : 객체마다 별도 존재

print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}' .format(a.name, a.age, b.name, b.age))


if a.species == 'firstdog':
    print('{0} is a {1}' .format(a.name, a.age))

print(a.species)

print(Dog.species)
print(b.species)


#예제 2

#self의 이해
class SelfTest:
    def func1(): #클래스 메소드
        print('Func1 Called')
    def func2(self):
        print(id(self))
        print('Func2 Called')


#self는 인스턴스를 요구한다. self에 f가 넘어간 것이다.

f = SelfTest()

# print(dir(f))
print(id(f))

#f.func1() : 예외

f.func2()

SelfTest.func1()

SelfTest.func2(f)


# 예제 3
#클래스 변수, 인스턴스 변수

class Warehouse:
    #클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        #인스턴습 변수
        self.name = name
        Warehouse.stock_num +=1

    def __del__(self):
        Warehouse.stock_num-=1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print('>>>>>>', user1.stock_num)
#인스턴스의 네임스페이스에서 못찾으면 클래스의 네임스페이스에서 찾아본다. 서로 공유하고 있기때문에

del user1
del user2
print('after', Warehouse.__dict__)



#예제 4

class Dog:  #Object 상속
    pass
    # 클래스 속성
    species = "firstdog" # 클래스 변수

    #초기화//인스턴스속성 #c++에서 생성자와 비슷
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old' .format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)




#인스턴스 생성

c = Dog('juicy', 4)
d = Dog('Merry', 10)
#메소드 호출
print(c.info())
print(d.info())

print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))








