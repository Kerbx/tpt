# for26 Прохоренков Егор ИСП-211.
x = float(input())
n = int(input())

_sum = 0

for i in range(n + 1):
    _sum += (-1) ** i * x ** (2 * i + 1) / (2 * i + 1)

print(_sum)