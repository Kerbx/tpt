import math

x = float(input())

if x < 0:
    print(0)
elif math.floor(x) % 2 == 0:
    print(1)
elif math.floor(x) % 2 != 0:
    print(-1)