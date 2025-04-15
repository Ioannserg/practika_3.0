def power_of(number, exponent=2):
    if exponent == 2:
        return print(f'Квадрат числа {number} в степени {exponent} равно {number ** exponent}')
    else:
        return print(f'Число {number} в степени {exponent} равно {number ** exponent}')

power_of(5, 3)
