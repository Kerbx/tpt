<<<<<<< HEAD
s = input()
s = s.split(sep=' ')
k = 0
for i in s:
    k += 1
    if i == '':
        k -= 1

print(k)
=======
print(list(input()).count(' '))
>>>>>>> ddb7541d810cd016527bcce556c22987a1025563
