# if24 Прохоренков Егор ИСП-211
import math

x = float(input())

if x > 0:
    print(2 * math.sin(x))
elif x <= 0:
    print(6 - x)