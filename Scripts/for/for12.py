# for12 Прохоренков Егор ИСП-211.
n = int(input())

_pow = 1

for i in range(1, n + 1):
    _pow *= 1 + i * 0.1

print(_pow)