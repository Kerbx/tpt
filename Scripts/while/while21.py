n = int(input())
bool = False
while n != 0:
    if n % 10 != 2:
        bool = True
    else:
        pass
    n //= 10

print(bool)