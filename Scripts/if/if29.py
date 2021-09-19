x = int(input())

description = ''

if x == 0:
    description = 'null'
elif x > 0:
    description += 'positive'
elif x < 0:
    description += 'negative'

if abs(x % 2) == 0:
    description += ' even'
elif abs(x % 2) != 0:
    description += ' odd'

print(description)
