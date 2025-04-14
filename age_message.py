def age_message(year):
    age = 2025 - year
    if age < 18:
        return print(f'Ваш возвраст: {age}\nВы еще молоды, учеба — ваш путь!')
    elif 18 < age < 65:
        return print(f'Ваш возвраст: {age}\nОтличный возраст для карьерного роста!')
    elif age > 65:
        return print(f'Ваш возвраст: {age}\nПора наслаждаться заслуженным отдыхом!')
    else:
        return print(f'Ваш возвраст: {age}\nчето ты мне пиздишь друг')
year = int(input('Введите год вашего рождения '))
age_message(year)

