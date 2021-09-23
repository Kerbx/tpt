a = int(input())
b = int(input())
s = a
_sum = 0

while s >= 0:
    s -= b
    _sum += 1

print(_sum - 1)