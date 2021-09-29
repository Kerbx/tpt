s = input()
s = s.split(sep=' ')
k = 0
for i in s:
    k += 1
    if i == '':
        k -= 1

print(k)