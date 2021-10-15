# for21 Прохоренков Егор ИСП-211.
import math

n = int(input())

_sum = 1

for i in range(1, n + 1):
    _sum += i/math.factorial(i)

print(_sum)