a = int(input())
b = int(input())

_pow = 0

for i in range(a, b + 1):
    _pow *= i

print(_pow)