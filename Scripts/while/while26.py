n = int(input())
f1 = 1
f2 = 1
fk = 0

while fk < n:
    fk = f1 + f2
    f2 = f1
    f1 = fk

print(f2, f1 + f2)
