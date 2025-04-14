def bubble_sort(*numbers):
    lst = []

    for i in numbers:
        lst.append(i)

    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return print(lst)

numbers = map(int, input('Введите числа через запятую ').split(','))
bubble_sort(*numbers)





