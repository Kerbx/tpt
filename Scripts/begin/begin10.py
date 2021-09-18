a = float(input())
b = float(input())

aSqrt = a ** 2
bSqrt = b ** 2

if a == 0 or b == 0:
    print('Число должно быть ненулевым.')
else:
    print(f'Сумма квадратов данных чисел: {aSqrt + bSqrt}\nРазность: {aSqrt - bSqrt}\nПроизведение: {aSqrt * bSqrt}\nЧастное: {aSqrt / bSqrt}')