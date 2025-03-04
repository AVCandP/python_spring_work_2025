# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо 
# и справа налево".



def number_chek(n):
    if str(n) == str(n)[0] * len(str(n)):
        return True
    else:
        return False
        
x = input('Введите любое четырехзначное число: ')
chek = number_chek(x) 

if chek == True:
    print(f'Высказываение истино')
else:
    print(f'Высказываение ложно')
