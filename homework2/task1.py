year = int(input("year to check: "))


def is_leap(year):
    leap = False

    if (year >= 1900 and year <= 100000):
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            leap = True
    else:
        print("%s is incorrect number. It must be from 1900 to 10000" % (year))

    return leap

print(is_leap(year))