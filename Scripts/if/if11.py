# if11 Прохоренков Егор ИСП-211
a = int(input())
b = int(input())
if a != b:
    a, b = max(a, b), max(a, b)
elif a == b:
    a, b = 0, 0

print(a, b)