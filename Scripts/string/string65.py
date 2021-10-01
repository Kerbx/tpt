text = input()
k = int(input())
f = lambda s: s[-k % len(s):] + s[:-k % len(s)]
_list = text.split()
decode = ' '.join([f(x) for x in _list])
print(decode)