# print 사용법

print('010','8777', '3234', sep='-')
print('c880910','naver.com', sep ='@')


#format 사용법(d,s,f)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))


print('%10s' %('nice')) #10개의 자리를 차지
print('{:>10}' .format('nice'))

print('%-10s' %('nice')) #10개의 자리를 차지
print('{:10}' .format('nice'))

print('{:$>10}' .format('nice'))
print('{:^10}' .format('nice')) #중앙정렬

print('%.5s' %('nice'))
print('%.5s' % ('pythonstudy')) #공간을 5개만차지하겠다는뜻
print('%5s' % ('pythonstudy')) #.을 안붙이면 공간 늘어남 .을 붙여야 절삭
print('{:10.5}' .format('pythonstudy')) #공간은 10개지만 5개만 출력한 것



# %d
print('%d %d' % (1,2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42))


# %f
print('%1.8f' %(3.123232)) #정수부 소수부 지정 가능
print('{:f}'.format(3.1443343243243))

print('%06.2f' %(3.141592665389793 ))
print('{:06.2f}' .format(3.1231323123))









