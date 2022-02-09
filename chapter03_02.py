#파이썬 문자형
#문자형 중요

str1 = "I am Python"
str2 = "Python"
str3 = """How are you"""
str4 = '''Thank you'''


print(len(str1))

#빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

#이스케이프 문자 사용

print('I\'m Boy')
print("I'm Boy")

escape_stt1 = "Do you have a \"retro games\"?"
print(escape_stt1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

#탭, 줄 바꿈
 

#Raw String
raw_s1 = r'D:\python\test' #r 이스케이프 문자열을 사용하지 않기 위해 사용

print(raw_s1)



# 멀티라인 입력
# 역슬래시 사용
multi_str = \
"""
String
Multi line
Test

"""

print(multi_str)


#문자열 연산

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

#대소문자 구별 가능
print(str_o1 *3)
print(str_o1+ str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66),type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

#문자열 함수(upper, isalnum, startswitch, count, endswitch, isalpha ...)

print("Capitalize : ", str_o1.capitalize())
print("endswitch? : ", str_o2.endswith("!"))
print("replace : ", str_o1.replace("thon  ", "Good"))
print("sorted : ", sorted(str_o1))
print("split :", str_o4.split(' ')) # 특정 문장을 분리할때

#반복(시퀀스)

im_str = "Good Boy"

#print(dir(im_str)) # iter 가 있으면 시퀀스 가능

#출력

for i in im_str:
    print(i)


# 슬라이싱 
str_s1 = "Nice Python"

#슬라이싱 연습
print(len(str_s1))

print(str_s1[0:3]) # 0 1 2
print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)]) #str_s1[:11]
print(str_s1[1:4:2])
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드)
a ='z'

print(ord(a))
print(chr(122))







