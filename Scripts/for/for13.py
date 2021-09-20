n = int(input())

_sum = 0

for i in range(1, n + 1):
    _sum += (1 + i * 0.1) * -1 ** (i + 1)

print(_sum)