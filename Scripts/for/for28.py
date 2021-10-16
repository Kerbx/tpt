# for28 Прохоренков Егор ИСП-211.
x = float(input())
n = int(input())

_sum = 1
sumOdd = 1
sumEven = 1

for i in range(1, n + 1):
    _sum += ((-1) ** (i - 1) * sumOdd * x ** i) / sumEven
    sumOdd *= (2 * i - 1)
    sumEven *= 2 * i
    print(f'-1 ** {i - 1} * {sumOdd} * {x ** i} / {sumEven}')
    
print(_sum)