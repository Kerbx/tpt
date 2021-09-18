a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
c1 = float(input())
c2 = float(input())

d = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / d
y = (a1 * c2 - a2 * c1) / d

print(f'x = {x}\ty = {y}')