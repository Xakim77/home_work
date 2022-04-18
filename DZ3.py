number = int(input('Введите число: '))
#исключения = 11 12 13 14
while number:
    if number == 12 or number == 13 or number == 14 or number == 11:
        print(str(number) + ' Процентов ')
        break
    elif number % 10 == 1:
        print(str(number) + ' Процент')
        break
    elif number % 10 > 1 and number % 10 < 5:
        print(str(number) + ' Процента')
        break
    else:
        print(str(number) + ' Процентов')
        break


