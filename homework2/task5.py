"""flip bits in number"""
NUMBER = int(input("number to convert: "))
CONVERTER = '1' * (len(bin(NUMBER))-2)
FLIP_NUMBER = NUMBER ^ int(CONVERTER, 2)
print(FLIP_NUMBER)
