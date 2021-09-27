e = float(input())

a1 = 1
a2 = 2
ak = 0
k = 2

while abs(a2 - a1):
    ak = a1
    a1 = a2
    k += 1
    a2 = (ak + 2 * a1) / 3

print(a1, a2)