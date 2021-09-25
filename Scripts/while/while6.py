n = float(input())
fact = 1

while n >= 2:
    fact *= n
    n -= 2

print(fact)