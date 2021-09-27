e = float(input())

a1 = 2
ak = 0
k = 1

while abs(a1 - ak) >= e:
    k += 1
    ak = a1
    a1 = 2 + 1/ak

print(k, ak, a1)