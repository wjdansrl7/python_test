#Chpater05_01
#파이썬 함수 및 중요성
#파이썬 함수식 및 람다(Lamda)

#함수 정의 방법
#def function_name(parameter):
#   code


#예제1
def first_func(w):
    print('Hello,', w)


word = 'Good boy'

first_func(word)



#예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)


#예제3(다중변환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x,y,z =  func_mul(10)

print(x,y,z)

#튜플 리턴


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))


#리스트 변환

def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul3(30)

print(type(p), p, set(p))



#딕셔너리 리턴

def func_mul4(x):
    y2 = x * 20
    y1 = x * 10
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul4(30)

print(type(d), d, d.get('v2'), d.items(), d.keys())

#중요
# *args, **kwargs

# *args(언팩킹)

def args_func(*args): #매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}' .format(i),v)
    print('------')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

#args에서 *를 붙이면 언팩킹으로 들어오는 인자들을 묶어서 하나의 자료구조로서 메소드 안에서 사용하게 해줄게
#하나의 튜플로 간주
#가변 인자를 사용할 수 있게 해줌

# **kwargs(언팩킹)

def kwargs_func(**kwargs):  #별표 두개는 딕셔너리 형태로 키와 밸류 값을 같이 넘겨준다라고 생각
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print()


kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Kim')

#전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3 = 40)


# 중첩함수 : 함수안에 함수가 있다.
# 중첩함수는 지역변수의 느낌으로 함수바깥에서 출력하면 출력되지 않는다.
def nested_func(num):
    def func_in_func(num): #선언부분
        print(num)
    print("In func")
    func_in_func(num+100)

nested_func(100)


#람다식 예제
#메모리 절약, 가독성 향상, 코드 간결
#함수 객체 생성 -> 리소스(메모리) 할당
#람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
#남발시 가독성 오히려 감소

# def mul_func(x, y):
#    return x *y

# lambda x, y:x*y

# 일반적함수 -> 할당
def mul_func(x, y):
    return x * y


print(mul_func(10, 50))
q = mul_func(10, 40)
print(q)

#람다함수 -> 할당

lambda_mul_func = lambda x, y:x*y

print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print('>>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x, y: x*y) #일시적으로 함수가 필요할때


















