from sys import *
import re

input_string = input("example to match: ")

input_s = input_string.strip()


def checker(input_str):
    pattern = "-{0,1}[0-9]{1,5}[*|/|+/-]-{0,1}[0-9]{1,5}=-{0,1}[0-9]{1,9}"
    result = ""
    p = re.compile(pattern)
    m = p.match(input_str)
    if m:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum_index = 0
        i = 0
        while i < len(input_str):
            if input_str[i] == '*':
                sum1 = int(input_str[0:i])
                sum_index = i
            elif input_str[i] == '/':
                sum1 = int(input_str[0:i])
                sum_index = i
            elif input_str[i] == '+':
                sum1 = int(input_str[0:i])
                sum_index = i
            elif input_str[i] == '-':
                if (i > 0) and (sum_index == 0):
                    sum1 = int(input_str[0:i])
                    sum_index = i
            elif input_str[i] == '=':
                sum2 = int(input_str[sum_index + 1:i])
                sum3 = int(input_str[i + 1:])
            i += 1
        if input_str[sum_index] == '*':
            if (sum1 * sum2) == sum3:
                result = "YES"
            else:
                result = "NO"
        elif input_str[sum_index] == '/':
            if sum2 != 0:
                if sum1 / sum2 == sum3 and sum1 % sum2 == 0:
                    result = "YES"
                else:
                    result = "NO"
            else:
                result = "NO"
        elif input_str[sum_index] == '+':
            if (sum1 + sum2) == sum3:
                result = "YES"
            else:
                result = "NO"
        elif input_str[sum_index] == '-':
            if sum1 - sum2 == sum3:
                result = "YES"
            else:
                result = "NO"
    else:
        result = "ERROR"
    return result


print(checker(input_s))
