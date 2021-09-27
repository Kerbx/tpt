n = int(input())
_sum = 0
k = 0

while n != 0:
    k += 1
    _sum += n % 10
    n //= 10

print(k, _sum)