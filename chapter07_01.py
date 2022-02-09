#Chapter07_01
#파이썬 예외처리의 이해
# 예외 종류
#SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ...

#문법적으로 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류

# NameError : 참조 없음
# a = 10
# b = 20
# print(c)

# ZeroDivisionError

# print(100/0)

# IndexError

# x = [70, 35, 23]
# print(x[1])
# print(x[4])

# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())


# KeyError
# dic = {'name' : 'Kee', 'Age' : 34, 'City' : 'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby')) 예외를 발생시키지 않음

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# #ValueError

# x = [10, 40, 90]
# x.remove(40)
# print(x)
# x.remove(300)

# FileNotFoundError

# f = open('test.txt')


# TypeError :  자료형에 맞지 않는 연산을 수행할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'Test'

# print(x + y)

# print(x + z)

# print(x + list(y))
# print(x + list(z))

# 예외 처리
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 :  여러 개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally :  항상 실행


#name = ['Kim', 'Lee', 'Park']

# 예제 1

# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it in name' .format(z, x+1))
# except ValueError:
#     print('Not found it! - Occured ValueError!')
# else:
#     print('OK! else.')



# 예제 2
# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it in name' .format(z, x+1))
# except Exception: #ValueError 이런식으로 입력해서 특정 예외를 잡아줄 수도 있고, 아무것도 입력하지 않으면 모든 예외처리를 잡는다.
#     print('Not found it! - Occured ValueError!')
# else:
#     print('OK! else.')

# 예제 3
# try:
#     z = 'Sim'
#     x = name.index(z)
#     print('{} Found it in name' .format(z, x+1))
# except Exception as e: #ValueError 이런식으로 입력해서 특정 예외를 잡아줄 수도 있고, 아무것도 입력하지 않으면 모든 예외처리를 잡는다.
#     print(e) #이런식으로 alias를 통해서 예외 내용을 확인함으로서 대략적으로 무슨 에외가 발생했는지 앟려줄 수 있다.
#     print('Not found it! - Occured ValueError!')
# else:
#     print('OK! else.')
# finally:
#     print('Ok! fianlly') #finally는 예외가 발생하든 발생하지 않든 맨 마지막에 무조건 출력해주는 실행

# print()

# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occured! Exceptional!')
else:
    print('OK! else')
    