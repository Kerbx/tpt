n = int(input())
fact = 1.0

while n >= 2:
    fact *= n
    n -= 2

print(fact)