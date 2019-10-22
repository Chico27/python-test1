# sub2.py
import sub3


def sub2func(testString):
    testString += '\nsub2 passed'
    return sub3.sub3func(testString)
