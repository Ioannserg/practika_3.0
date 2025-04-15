def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return print(f'Число {number} положительное и четное')
        else:
            return print(f'Число {number} положительное и нечетное')
    elif number == 0:
        return print(f'Число {number} не туда не сюда')
    else:
        return print(f'Число {number} отрицательное')

check_number(-2)