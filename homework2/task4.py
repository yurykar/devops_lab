"""check words in dictionary"""
from collections import defaultdict

NUMBER = input("input number of n and m: ")
n, m = NUMBER.split()
WORDS = []
WORDS_CHECK = []
print("input %s words for group A" % n)
WORDS = [input() for _ in range(int(n))]
print("input %s words for group B" % m)
WORDS_CHECK = [input() for _ in range(int(m))]

DEF_DIC = defaultdict(list)
if 1 <= int(n) <= 10000 and 1 <= int(m) <= 100:
    for i in range(int(n)):
        if 1 <= len(WORDS[i]) <= 100:
            DEF_DIC[WORDS[i]].append(i+1)
        else:
            print("length of word %s should be from 1 to 100" % (WORDS[i]))
    for i in range(len(WORDS_CHECK)):
        if WORDS_CHECK[i] in DEF_DIC:
            print(*DEF_DIC[WORDS_CHECK[i]], sep=' ')
        else:
            print("-1")
else:
    print("n should be from 1 to 10000. m should be from 1 to 100")
