n = int(input())
a1 = 1
a2 = 2

for i in range(3, n + 1):
    print((a1 + a2 * 2) / 3)
    a1 = (a1 + a2 * 2) / 3
    a2 = (a1 + a2 * 2) / 3
    print(a2)