# for33 Прохоренков Егор ИСП-211.
n = int(input())

f1 = 1
f2 = 1
print(f1)
print(f2)

for i in range(3, n + 1):
    print(f1 + f2)
    f1 = f1 + f2
    f2 = f1 + f2
    print(f2)