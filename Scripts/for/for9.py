# for9 Прохоренков Егор ИСП-211.
a = int(input())
b = int(input())

_sum = 0

for i in range(a, b + 1):
    _sum += i ** 2

print(_sum)