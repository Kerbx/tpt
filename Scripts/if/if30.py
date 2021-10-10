# if30 Прохоренков Егор ИСП-211
x = int(input())

description = ''

if 0 < x < 9:
    description += '1-number'
elif 9 < x < 99:
    description += '2-number'
elif x > 99:
    description += '3-number'

if x % 2 == 0:
    description += ' even'
elif x % 2 != 0:
    description += ' odd'

print(description)