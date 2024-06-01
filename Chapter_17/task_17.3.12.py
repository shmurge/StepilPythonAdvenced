# Вам доступен текстовый файл file.txt, набранный латиницей.
# Напишите программу, которая выводит количество букв латинского алфавита, слов и строк.
# Выведите три найденных числа в формате, приведенном в примере.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.


letters = 0
words = 0
lines = 0
with open('file.txt') as file:
    for line in file:
        ls = line.strip().split()
        words += len(ls)
        lines += 1
        for word in ls:
            for letter in word:
                if letter.isalpha():
                    letters += 1

print(f'Input file contains: \n{letters} letters \n{words} words \n{lines} lines')
