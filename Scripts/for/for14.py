# for14 Прохоренков Егор ИСП-211.
n = int(input())

_sum = 0

for i in range(1, n + 1):
    _sum += 2 * i - 1
    print(_sum)

print(_sum)