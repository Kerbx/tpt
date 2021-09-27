n = int(input())
f1 = 1
f2 = 1
fk = 0
k = 2

while fk < n + 1:
    k += 1
    fk = f1 + f2
    f2 = f1
    f1 = fk
print(k)
