# for27 Прохоренков Егор ИСП-211.
x = float(input())
n = int(input())

_sum = x
powOdd = 1
powEven = 1

for i in range(1, n + 1):
    _sum += powOdd * x ** (2 * i + 1) / (powEven * (2 * i + 1))
    powOdd *= 2 * i - 1
    powEven *= 2 * i

print(_sum)
