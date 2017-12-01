from sys import *
import re

inputString = input("example to match: ")

input = inputString.lstrip().rstrip()

def checker(input):
    pattern = "-{0,1}[0-9]{1,5}[*|/|+/-]-{0,1}[0-9]{1,5}=-{0,1}[0-9]{1,9}"
    result = ""
    p = re.compile(pattern)
    m = p.match(input)
    if m:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sumIndex = 0
        i = 0
        while i < len(input):
            if input[i] == '*':
                sum1 = int(input[0:i])
                sumIndex = i
            elif input[i] == '/':
                sum1 = int(input[0:i])
                sumIndex = i
            elif input[i] == '+':
                sum1 = int(input[0:i])
                sumIndex = i
            elif input[i] == '-':
                if (i > 0) and (sumIndex == 0):
                    sum1 = int(input[0:i])
                    sumIndex = i
            elif input[i] == '=':
                sum2 = int(input[sumIndex + 1:i])
                sum3 = int(input[i + 1:])
            i += 1
        if input[sumIndex] == '*':
            if (sum1 * sum2) == sum3:
                result = "YES"
            else:
                result = "NO"
        elif input[sumIndex] == '/':
            if sum2 != 0:
                if ((sum1 / sum2) == sum3) and ((sum1 % sum2) == 0):
                    result = "YES"
                else:
                    result = "NO"
            else:
                result = "NO"
        elif input[sumIndex] == '+':
            if (sum1 + sum2) == sum3:
                result = "YES"
            else:
                result = "NO"
        elif input[sumIndex] == '-':
            if (sum1 - sum2) == sum3:
                result = "YES"
            else:
                result = "NO"
    else:
        result = "ERROR"
    return result

print(checker(input))