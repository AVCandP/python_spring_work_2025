# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

x = float(input('Задайте коэффициент А: '))

if x == 0:
    print('А не может быть равно 0. Введите параметр снова:')
    x = float(input('Задайте коэффициент А: '))
    while x == 0:
        print('А не может быть равно 0. Введите параметр снова:')
        x = float(input('Задайте коэффициент А: '))
else:
    pass

y = float(input('Задайте коэффициент B: '))

result = -y/x

print(f'решение уровнения A·x + B = 0 равно: x = {result:.3f}')