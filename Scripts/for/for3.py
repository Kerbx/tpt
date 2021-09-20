a = int(input())
b = int(input()) - 1

_sum = 0

for i in range(b - a):
    print(b - _sum)
    _sum += 1

print(_sum)
