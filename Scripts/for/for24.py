# for24 Прохоренков Егор ИСП-211.
import math

x = float(input())
n = int(input())

_sum = 0

for i in range(0, n + 1):
    _sum += (-1) ** i * x ** (2 * i) / math.factorial(2 * i)

print(_sum)