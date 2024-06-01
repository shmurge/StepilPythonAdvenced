# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

# Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их,
# каждую на отдельной строке.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.

from random import *

with open('first_names.txt') as file1, open('last_names.txt') as file2:
    firstnames = [i.strip() for i in file1.readlines()]
    surnames = [j.strip() for j in file2.readlines()]
    for _ in range(3):
        print(firstnames[randint(0, len(firstnames))], surnames[randint(0, len(surnames))])
