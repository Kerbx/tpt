# if16 Прохоренков Егор ИСП-211
a = float(input())
b = float(input())
c = float(input())

if a < b < c:
    a, b, c = a * 2, b * 2, c * 2
else:
    a, b, c = a * -1, b * -1, c * -1

print(a, b, c)