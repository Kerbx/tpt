# for18 Прохоренков Егор ИСП-211.
a = float(input())
n = int(input())

_sum = 0

for i in range(0, n + 1):
    _sum += ((-1) ** i) * a ** i
print(_sum)