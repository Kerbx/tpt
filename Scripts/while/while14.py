a = int(input())
k = 1
_sum = 0

while a > _sum:
    k += 1
    _sum += 1/k

print(k - 1, _sum - 1/k)