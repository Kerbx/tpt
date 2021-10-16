n = int(input())
k = 0
_sum = 0

while n - k >= _sum + k:
    k += 1
    _sum += k

print(k, _sum)