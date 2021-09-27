n = int(input())
r = ''

while n != 0:
    r += str(n % 10)
    n //= 10

print(int(r))