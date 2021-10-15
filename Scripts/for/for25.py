# for25 Прохоренков Егор ИСП-211.
x = float(input())
n = int(input())

_sum = 0

for i in range(n + 1):
    _sum += -1 ** (i - 1) * x ** i / i

print(_sum)