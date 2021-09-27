p = float(input()) * 0.01
f = 10
s = 10
k = 1

while s <= 200:
    k += 1
    f += f * p
    s += f

print(k, s)