a = int(input())
b = int(input())
c = int(input())

_list = [a, b, c]
_list.remove(max(a, b, c))
_list.remove(min(a, b, c))

print(_list[0])