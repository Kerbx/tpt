s = input()
s = s.split(sep=' ')
k = []

for i in s:
    if i != '':
        k.append(len(i))

print(min(k))