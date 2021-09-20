import math

x = float(input())
n = int(input())

_sum = 0

for i in range(1, n + 1):
    _sum += x ** i / math.factorial(i)

print(_sum)