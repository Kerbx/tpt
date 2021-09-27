a = int(input())
b = int(input())
c = int(input())
k = 0

while a - c >= 0:
    a -= c
    bt = b
    while bt - c >= 0:
        bt -= c
        k += 1

print(k)
