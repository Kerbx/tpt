a = float(input())
b = float(input())
c = float(input())
discr = b ** 2 - 4 * a * c
x1 = (-b + discr ** 0.5) / (2 * a)
x2 = (-b - discr ** 0.5) / (2 * a)
print(f'x1 = {x1}\tx2 = {x2}')