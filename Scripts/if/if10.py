a = int(input())
b = int(input())
if a != b:
    a, b = a + b
elif a == b:
    a, b = 0

print(a, b)