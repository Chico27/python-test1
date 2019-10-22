import sub2


def sub1func(testString):
    testString += '\nSub1 passed'
    return sub2.sub2func(testString)

