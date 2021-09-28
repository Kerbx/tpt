s = input()

if s.isdecimal():
    print(1)
elif '.' in s:
    print(2)
else:
    print(0)