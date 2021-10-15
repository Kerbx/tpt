# for29 Прохоренков Егор ИСП-211.
n = int(input())
a = float(input())
b = float(input())

ab = b - a
print(ab / n)

for i in range(int(ab / n + 1)):
    print(a + (ab / n) * i)