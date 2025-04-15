def check_string_length(string, length):
    if len(string) >= length:
        return print(f'Длинна строки достаточная')
    else:
        return print(f'Строка слишком короткая')

check_string_length('банана', 7)