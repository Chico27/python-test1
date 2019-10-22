import traceback

def sub3func(testString):
    testString += '\nsub3 passed'

    print("".join(traceback.format_stack()))

    return testString
