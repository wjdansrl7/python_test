#Chapter05_02
#파이썬 사용자 입력
#input 사용법
#기본 타입(Str)

#예제1
#name = input("Enter your name")
#grade = input("Enter your Grade")
#company = input("Enter your company name")

#print(name, grade, company)

#예제2
#number = input("Enter your number : ")
#name = input("Enter your name")

#print("Type of number : ", type(number))
#print("Type of number : ", type(name))


#예제3(계산)

first_number = int(input("Enter your number1 : "))
second_number = int(input("Enter your number2 : "))

total = first_number + second_number

print('first_number + second_number : ', total )


#예제4
float_number = float(input("Enter a float number : "))

print('input float : ', float_number)
print('input type : ', type(float_number))


#예제5
print("FirstName - {0}, LastName - {1}" .format(input("Enter first name : "), input("Enter second name : ")))

