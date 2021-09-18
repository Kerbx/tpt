x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())

if abs(x - x1) == 1 and abs(y - y1) == 2 or abs(x - x1) == 2 and abs(y - y1) == 1:
    print('True.')
else:
    print('False.')