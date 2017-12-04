from collections import defaultdict

number = input("input number of n and m: ")
n, m = number.lstrip().rstrip().split()
words = []
wordsToCheck = []
print("input %s words for group A" % (n))
while True:
    line = input()
    if line:
        words.append(line)
    else:
        break
print("input %s words for group B" % (m))
while True:
    line = input()
    if line:
        wordsToCheck.append(line)
    else:
        break


d = defaultdict(list)
if 1 <= int(n) <= 10000 and 1 <= int(m) <= 100:
    for i in range(int(n)):
        if 1 <= len(words[i]) <= 100:
            d[words[i]].append(i)
        else:
            print("length of word %s should be from 1 to 100" % (words[i]))
    for i in range(len(wordsToCheck)):
        if wordsToCheck[i] in d:
            print(d[words[i]])
        else:
            print("-1")
else:
    print("n should be from 1 to 10000. m should be from 1 to 100")
