# for37 Прохоренков Егор ИСП-211.
n = int(input())

_sum = 0.0

for i in range(1, n + 1):
    _sum += i ** i

print(_sum)