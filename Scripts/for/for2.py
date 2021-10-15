# for2 Прохоренков Егор ИСП-211.
a = int(input())
b = int(input())

_sum = 0

for i in range(b - a + 1):
    print(b - _sum)
    _sum += 1

print(_sum)
