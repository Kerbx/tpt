a = float(input())
b = float(input())
c = float(input())

if a < b < c:
    a, b, c *= 2
else:
    a, b, c *= -1

print(a, b, c)