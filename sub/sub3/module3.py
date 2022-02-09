import sys
import inspect

def mod3_test1():
    print('Module3-> Test1')
    print('Path :', inspect.getfile(inspect.currentframe()))


def mod3_test2():
    print('Module3 -> Test2')
    print('Path : ', inspect.getfile(inspect.currentframe()))

    