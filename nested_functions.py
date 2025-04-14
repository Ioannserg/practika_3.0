def calculator():
    def oper1(num1, num2):
        print(num1+num2)

    def oper2(num1, num2):
        print(num1 - num2)

    def oper3(num1, num2):
        print(num1 * num2)

    def oper4(num1, num2):
        print(num1 / num2)

    num1 = int(input('Введите число 1: '))
    num2 = int(input('Введите число 2: '))
    operat = input('Выберите операцию (+, -, *, /): ')
    if operat == '+':
        oper1(num1, num2)
    elif operat == '-':
        oper2(num1, num2)
    elif operat == '*':
        oper3(num1, num2)
    elif operat == '/':
        oper4(num1, num2)
    else:
        print('Ты выбрал хуйню давай по новой')

calculator()