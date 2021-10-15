# for40 Прохоренков Егор ИСП-211.
a = int(input())
b = int(input())

for i in range(1, b - a + 2):
    for t in range(i):
        print(a + i - 1)