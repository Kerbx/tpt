x = float(input())
n = int(input())

_sum = 1
powOdd = 1
powEven = 1

for i in range(1, n + 1):
    powOdd *= 2 * i - 3 
    powEven *= 2 * i
    _sum += -1 ** (i - 1) * powOdd * x ** i / powEven

print(_sum)