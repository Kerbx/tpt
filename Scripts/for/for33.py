n = int(input())

f1 = 1
f2 = 1

for i in range(3, n + 1):
    print(f1 + f2)
    f1 = f1 + f2
    f2 = f1 + f2
    print(f2)