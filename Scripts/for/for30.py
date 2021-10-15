# for30 Прохоренков Егор ИСП-211.
import math

n = int(input())
a = float(input())
b = float(input())

ab = b - a
print(ab / n)

for i in range(int(ab / n + 1)):
    print(1 - math.sin(a + (ab / n) * i))