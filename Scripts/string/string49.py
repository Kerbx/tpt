s = input()
sn = s.split(sep=' ')
k = 0

for i in sn:
    for q in i:
        if q == i[-1]:
            k += 1
    if i != '':
        s = s.replace(i, i.replace(i[-1], '.', k - 1))
    k = 0

print(s)