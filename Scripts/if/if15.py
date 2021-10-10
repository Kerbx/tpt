# if15 Прохоренков Егор ИСП-211
a = int(input())
b = int(input())
c = int(input())

if min(a, b, c) == a:
    print(b + c)
elif min(a, b, c) == b:
    print(a + c)
elif min(a, b, c) == c:
    print(a + b)