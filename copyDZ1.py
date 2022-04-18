
# Здравствуйте ! я максимально старался уменьшить колл-во строк в коде (это максимум что я смог)
duration = int(input('Введите число: '))
minute = 60
hour = 3600
day = 86400
if duration < minute :
    print(str(duration) + ' секунд')
elif duration >= minute and duration < hour:
    print(str(duration // minute) + ' минут(ы) ' + str(duration % minute) + ' секунд(ы)')
elif duration >= hour and duration < day:
    amout_hour = duration // hour # колличство  часов
    remainder_minute = duration % hour # остаток времени
    amout_minute = remainder_minute // minute #колличесво минут
    amout_second = remainder_minute % minute # колличесво секунд
    print(str(amout_hour) + ' час(а) ' + str(amout_minute) + ' минут(ы) ' + str(amout_second) + ' секунд(ы)')
elif duration >= day:
    amout_day = duration // day # колличесво дней
    remainder_time = duration % day # остаток времени
    amout_hour = remainder_time // hour # колличесво часов
    remainder_time_2 = remainder_time %  hour
    amout_minute = remainder_time_2 // minute # колличесво минут
    amout_sekond = remainder_time_2 % minute #колличесво секунд
    print(str(amout_day) + ' день(я) ' + str(amout_hour) + ' час(а) ' + str(amout_minute) + ' минут(ы) ' + str(amout_sekond) + ' секунд(ы)')





