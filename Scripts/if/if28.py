# if28 Прохоренков Егор ИСП-211
n = int(input())

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(366)
else:
    print(365)