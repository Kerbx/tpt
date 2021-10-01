s = input()
s = s.split()
k = 0

for i in s:
    if i == '.' or ',' or '!' or '?' or ':':
        k += 1

print(k)