# for20 Прохоренков Егор ИСП-211.
n = float(input())

_sumFactor = 0

for i in range(1, int(n + 1)):
    factor = 1
    for p in range(1, int(i + 1)):
        factor *= p
    _sumFactor += factor

print(_sumFactor)