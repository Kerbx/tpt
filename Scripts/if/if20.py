# if20 Прохоренков Егор ИСП-211
a = int(input())
b = int(input())
c = int(input())

if abs(b) - abs(a) > abs(c) - abs(a):
    print('c', abs(c) - abs(a))
else:
    print('b', abs(b) - abs(a))