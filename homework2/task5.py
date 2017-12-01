number = int(input("number to convert: "))

converter = ''.join([str(1) for i in range(len(bin(number))-2)])
flipNumber = number ^ int(converter, 2)
print(flipNumber)


