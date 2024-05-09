#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)
    print(result)

uppercase("best")
uppercase("Best School 98 Battery street")
