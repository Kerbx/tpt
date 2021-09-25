n = int(input())
k = 0

while n > 3 ** k:
    k += 1

print(k + 1)