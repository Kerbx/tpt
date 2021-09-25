# Integer29 Прохоренков Егор ИСП-211
a = int(input())
b = int(input())
c = int(input())

sqrt1 = a * b
sqrt2 = c ** 2

a = int(a / c)
b = int(b / c)

print(a * b, sqrt1 - a * b * sqrt2)