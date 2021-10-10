# if23 Прохоренков Егор ИСП-211
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = 0
y3 = 0

if x1 == x2: x3 = x
elif x2 == x: x3 = x1
elif x == x1: x3 = x2

if y1 == y2: y3 = y
elif y2 == y: y3 = y1
elif y == y1: y3 = y2

print(x3, y3)