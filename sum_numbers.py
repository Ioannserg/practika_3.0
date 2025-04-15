def sum_numbers(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return print(f'Сумма чисел от 1 до {n}: {sum}')

sum_numbers(5)