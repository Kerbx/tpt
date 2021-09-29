c = input()
s = input()
s0 = input()
stmp = ''

for i in s:
    if i == c:
        stmp += s0
    stmp += i

print(stmp)