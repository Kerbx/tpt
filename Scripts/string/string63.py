abc = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
text = input()
k = int(input())

ans = ''
notuse = ',.!?:;\'" '
text = text.lower().replace('ё','е')
for i in text:
    if i not in notuse:
        index = k + abc.index(i)
        if index >= 32:
            index = index - 33 * (index // 33)
        ans += (abc[index].upper())
    else:
        ans += i
print(ans)