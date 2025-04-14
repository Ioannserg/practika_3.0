def check_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        return print('С этими параметрами сторон нельзя построить треугольник')
    elif a == b == c:
        return print('Результат: Треугольник равносторонний')
    elif a == b or a == c or b == c:
        return print('Результат: Треугольник равнобедренный')

    else:
        return print('Результат: Треугольник разносторонний')

a = int(input('Введите сторону а '))
b = int(input('Введите сторону b '))
c = int(input('Введите сторону c '))
check_triangle(a, b, c)
