# sub1.py
import sub2
import inspect


def sub1func(testString):
    testString += '\nSub1 passed'

    # print('')
    # print('呼び出し元のファイル')
    # print(inspect.currentframe().f_back.f_code.co_filename)
    # print('呼び出し元のライン')
    # print(inspect.currentframe().f_back.f_lineno)
    #
    # return testString
    return sub2.sub2func(testString)

