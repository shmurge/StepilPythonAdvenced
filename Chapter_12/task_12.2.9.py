# Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит
# их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.

import random


def lottery_ticket_numbers():
    numbers_list = list()

    while len(numbers_list) != 100:
        number = list()

        while len(number) != 7:
            if len(number) == 0:
                num = random.randint(1, 9)
            else:
                num = random.randint(0, 9)
            number.append(num)

        if number not in numbers_list:
            numbers_list.append(number)

    return numbers_list


ls = lottery_ticket_numbers()

for i in ls:
    print(*i, sep='')
