# for8 Прохоренков Егор ИСП-211.
a = int(input())
b = int(input())

_pow = 1

for i in range(a, b + 1):
    _pow *= i

print(_pow)