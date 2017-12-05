N = int(input("number to check: "))


def number(num):
    if 0 <= num <= 10**9:
        out = -1
        for i in range(10**9):
            fol = list(str(i))
            com = 1
            for y in fol:
                if y != 0:
                    com *= int(y)
            if com == num:
                out = i
                break

    else:
        out = -1
    return out


print(number(N))

