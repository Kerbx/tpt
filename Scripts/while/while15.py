n = 1000
p = float(input()) * 0.01
k = 1

while n < 1100:
    n *= k * p
    k += 1

print(k, n)