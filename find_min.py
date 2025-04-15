def find_min(numbers):
    min = 0
    for i in numbers:
        if i < numbers[0]:
            min = i
    return print(min)

find_min([1, 4, 6, 3, 0, 100, -4])