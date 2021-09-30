s = list(input())
sn = ''
sEven = s[0:len(s) // 2]
sOdd = s[len(s) // 2:]
k = 0

for i in sEven:
    sn += sOdd[-(k + 1)] + sEven[k]
    k += 1

if len(sOdd) % 2 != 0:
    sn += sOdd[0]

print(sn)