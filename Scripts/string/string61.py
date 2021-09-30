s = input().split(sep='\\')
k = len(s) - 1

if k == 1:
    print('\\')
else:
    print(s)
    print(s[-2])