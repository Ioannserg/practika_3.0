def convert_seconds(sek):
    hours = (sek // 3600)
    minutes = (sek % 3600) // 60
    tupple = (hours, minutes)
    return print(f'В {sek} секундах содержится {hours} час и {minutes} минут {tupple}')
convert_seconds(3672)




