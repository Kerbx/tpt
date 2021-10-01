s = input().split(sep=('/'))
k = ''
for i in s:
    if '.' in i:
        k = i
        break

print(k.split(sep='.')[-1])