def multiplication_table():
    result = ''
    for i in range(1, 11):
        for j in range(1, 11):
            digit = i * j
            result += str(digit) + ' '
        result += '\n'
    print(result)
multiplication_table()