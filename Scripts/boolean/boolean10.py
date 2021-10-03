# boolean10 Прохоренков ИСП-211
a = int(input())
b = int(input())
if (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0):
    print('Истина.')
else:
    print('Ложь.')