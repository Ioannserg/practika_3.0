def check_grade(score):
    if 0 <= score < 50:
        return print(f'Ваша оценка: {score}. Неудовлетворительно')
    elif 50 <= score <= 74:
        return print(f'Ваша оценка: {score}. Удовлетворительно')
    elif 75 <= score <= 89:
        return print(f'Ваша оценка: {score}. Хорошо')
    elif 90 <= score <= 100:
        return print(f'Ваша оценка: {score}. Отлично')
    else:
        return print(f'Не пизди')

check_grade(101)
