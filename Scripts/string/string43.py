s = input()
s = s.split(sep=' ')
k = 0

for i in s:
    if 'A' in i:
        k += 1

print(k)