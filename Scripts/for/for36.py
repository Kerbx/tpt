n = float(input())
k = float(input())

_sum = 0

for i in range(int(n + 1)):
    _sum += i ** k

print(_sum)