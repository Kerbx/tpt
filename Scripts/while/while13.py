a = int(input())

k = 1
_sum = 0

while _sum < a:
    _sum += 1/k
    k += 1

print(k, _sum)