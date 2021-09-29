s = input()
s = s.split(' ')
s = sorted(s)
for i in s:
    if i != '':
        print(i, end=' ')