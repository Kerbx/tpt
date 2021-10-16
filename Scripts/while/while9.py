n = int(input())
k = 0

while 3 ** k < n + 1:
    k += 1

print(k + 1)