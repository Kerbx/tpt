a = float(input())
n = int(input())

_sum = 0

for i in range(n + 1):
    _sum += -1 ** i * a ** i

print(_sum)