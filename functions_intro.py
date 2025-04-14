def greet_user(name):
    print(f'Привет, {name}! Добро пожаловать в мир Пайтон')


def calculate_sum(a, b):
    print(f'Сумма чисел: {a+b}')


name = input('Введите ваше имя ')
greet_user(name)
a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
calculate_sum(a, b)
