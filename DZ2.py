number = 0
nakop_summ = 0
number_max = 1000
while number <= number_max:
    if number % 2 != 0:
        kube = number**3
        summa = 0
        while kube > 0:
            digit = kube % 10
            summa = summa + digit
            kube = kube // 10
        if summa % 7 == 0:
            nakop_summ += number
            print(str(number) + '^3 = ' +str(number**3) + str([summa]) + 'накоп.сумма:' + str(nakop_summ))




    number += 1
