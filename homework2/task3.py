N = int(input("number to check: "))
def number(N):
    if 0 <= N <= 10**9:
        Q = -1
        for i in range(10**9):
            f = [x for x in str(i)]
            d=1
            for y in range(len(f)):
                d *= int(f[y])
            if d == N:
                Q = i
                break

    else:
        Q = -1
    return Q

print(number(N))
