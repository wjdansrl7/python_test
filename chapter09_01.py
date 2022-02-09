# Chapter09_01
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 a, 텍스트 모드 : t, 바이너리 모드 : b
#상대 경로(../, ./) 절대 경로(C:\users)

#파일 읽기(Read)

#예제 1

f = open('./resource/it_news.txt','r', encoding='UTF=8')

#속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

#파일 이름
print(f.name)

#모드 확인
print(f.mode)

cts = f.read()
print(cts)
#반드시 close
f.close()

# 예제 2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    #print(list(c)) # with를 사용하면 close를 사용하지 않아도 됨

print()

# 예제 3
# read() : 전체 읽기, read(10) : 10Byte

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c) #커서가 내부에 있어서 어디까지 읽었는지 기억함

    c = f.seek(0,0) #from to
    c = f.read(20)
    print(c)

    #print(iter(c))


# 예제 4
# readline : 한 줄 씩 읽기

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


print()

# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
# 자주 쓰임
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
    
print()

# 파일 쓰기(write)

with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

 # 예제 2
with open('./resource/contents1.txt', 'a') as f: # a:append를 쓰면 뒤에 입력, w로 입력시 초기화되서 새로 입력된다.
    f.write('I love python2\n')


# 예제 3
# writelines : 리스트 -> 파일 중요 ****

with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)


# 예제 4 print문으로 출력하는 건데 콘솔에 출력되지않고 파일에 출력된다.
with open('./resource/contents2.txt', 'w') as f:
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
    
  
