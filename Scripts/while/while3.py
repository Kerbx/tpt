n = int(input())
k = int(input())
i = 0
s = 0

while n >= k:
    n -= k
    s += 1

print(s, n)
