n = int(input())
k = 2

while k < n - 1 and n % k != 0:
    k += 1

if n % k != 0:
    print('True.')
else:
    print('False.')