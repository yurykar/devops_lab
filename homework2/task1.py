"""check leap year"""
YEAR = int(input("year to check: "))


def is_leap(year_check):
    """check leap year"""
    leap = False

    if 1900 <= year_check <= 100000:
        if (year_check % 4 == 0 and year_check % 100 != 0) or year_check % 400 == 0:
            leap = True
    else:
        print("%s is incorrect number. It must be from 1900 to 10000" % year_check)

    return leap


print(is_leap(YEAR))
