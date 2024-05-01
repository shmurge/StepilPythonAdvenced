# Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).
#
# Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
# Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.
#
# Примечание. Убедитесь, что сгенерированные числа не содержат дубликатов.

import random


def lottery_ticket_numbers():
    number = set()

    while len(number) != 7:
        num = random.randint(1, 49)
        number.add(num)

    number = sorted(list(number))

    return number

print(*lottery_ticket_numbers())
