#Chapter10_02
#Hangman(행맨) 미니 게임 제작(2)
# 기본 프로그램 제작 및 최종 테스트

import time
# csv 처리
import csv
# 랜덤
import random
# 사운드 처리
#import winsound
import pygame

#처음 인사
name = input("What is your name? ")

print('Hi ' + name + 'Time to play hangman game!')

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)
# CSV 단어 리스트
words = []
#문제 CSV 파일 로드
with open('./resource/word_list.csv','r', encoding='utf-8') as f:
    reader = csv.reader(f)
    # Header Skip
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words) 

# print(q) q로 출력하면 index 0,1에 키와 밸류가 같이 나오므로


# 정답 단어
word = q[0].strip()


#추측 단어
guesses = ''

#기회
turns = 10

#핵심 While Loop
#찬스 카운터가 남아 있을 경우

while turns > 0:
    #실패 횟수(단어 매치 수)
    failed = 0

    #정답 단어 반복
    for char in word:
        #정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            print(char,end=' ')
        else:
            #틀린 경우 대시로 처리
            print("_",end=' ')
            failed+=1
        #단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        #winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulation! The Guesses is correct')
        # while 구문 중단
        break
    print()


    #추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character ")


    #단어 더하기
    guesses +=guess

    #정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns-=1
        #오류 메시지
        print("Oops! Wrong")
        #남은 기회 출력
        print("You have", turns, 'more guesses!')

        if turns == 0:
            #실패 메시지
        #winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print("You hangman game failed. Bye!")




