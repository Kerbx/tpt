a = float(input())
b = float(input())

if a < 0 or b < 0:
    print('Числа не должны быть отрицательными.')
else:
    print(f'Среднее геометрическое равняется: {(a * b) ** 0.5}')