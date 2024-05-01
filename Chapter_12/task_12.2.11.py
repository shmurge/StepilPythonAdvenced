# Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные)
# целые числа от 1 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).

# Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.

# Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 3 символа.
# Для этого используйте строковый метод ljust().

# Примечание 2. Пример возможного ответа:

# 1  16 31 46 61
# 10 30 42 47 68
# 3  18 0  48 63
# 9  19 34 49 70
# 5  20 35 50 65

# Возможны и другие способы генерации карточки для игры в бинго.

import random


def bingo_card_generator():
    bingo_card = [[] for i in range(5)]
    archive = list()

    for i in range(len(bingo_card)):

        while len(bingo_card[i]) != 5:
            num = random.randint(1, 75)
            if num not in archive:
                bingo_card[i].append(num)
                archive.append(num)
            else:
                continue

        bingo_card[i].sort()

    bingo_card[2][2] = 0

    for i in range(len(bingo_card)):

        for j in range(len(bingo_card[i])):
            print(str(bingo_card[i][j]).ljust(3), end='')
        print()


bingo_card_generator()