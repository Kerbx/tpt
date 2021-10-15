# for28 Прохоренков Егор ИСП-211.
x = float(input())
n = int(input())

_sum = 1

for i in range(1, n + 1):
    _sum += (-1) ** (i - 1) * (2 * i - 3) * x ** i / 2 * i

print(_sum)