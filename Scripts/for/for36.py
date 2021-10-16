# for36 Прохоренков Егор ИСП-211.
n = int(input())
k = int(input())

_sum = 0.0

for i in range(int(n + 1)):
    _sum += i ** k

print(_sum)