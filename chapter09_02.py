#Chapter09_02
#CSV 파일 읽기 및 쓰기
# CSV -text/html

import csv

# 예제 1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Header Skip
    #객체 확인
    print(reader)
    #타입 확인
    print(type(reader))

    #속성 확인
    print(dir(reader)) #__iter__
    print()

    for c in reader:
        #print(c)
        #타입 확인(리스트)
        #print(type(c))
        #list to str
        print(' : '.join(c)) #리스트 형태를 보기 좋게 만들 수 있다.

# 예제 2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)


# 예제 3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k, v in c.items():
            print(k,v)
        print('----------')

# 예제 4
w = [[1,2,3], [4,5,6], [7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv','w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    #print(dir(wt))
    #타입 확인
    #print(type(wt))

    for v in w:
        wt.writerow(v) #리스트안에 있는 각각의 리스트가 하나의 레코드로 이용

# 예제 5
with open('./resource/write2.csv','w', encoding='UTF-8') as f:
    #필드명
    fields = ['One', 'Two', 'Three']

    #Dict Writer
    wt = csv.DictWriter(f, fieldnames=fields)
    #Header Writer
    wt.writeheader() #csv 파일에 헤더를 적어주는 것

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2] })

#csv 파일은 데이터 전처리나 이런데서 종종 쓰임, database 대신 쓸 수 있긴 한데 귀칞음













    
