def number_sum(n):
    result = ''
    a = 0
    sum = 0
    while a != n:
        a += 1
        result += str(a) + ' '
        sum += a
    print(f'Числа: {result} \nСумма цифр = {sum}')

n = int(input('Введите число: '))
number_sum(n)