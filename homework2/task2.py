"""made list with unique elements"""
print("input number for list A")
A = []
while True:
    line = input()
    if line:
        A.append(line)
    else:
        break
print("input number for list B")
B = []
while True:
    line = input()
    if line:
        B.append(line)
    else:
        break
C = set.union(set(A), set(B))
print(sorted(C))
