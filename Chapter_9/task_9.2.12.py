# Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года. Для каждого урока есть листок со списком присутствовавших учеников.
#
# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.
#
# Формат входных данных
# На вход программе в первой строке дается число m – количество уроков, проведенных с начала учебного года.
# Далее идёт m блоков строк, описывающих листки с фамилиями. На первой строке каждого блока указано количество фамилий
# n(i) , затем идёт n(i) строчек с фамилиями тех, кто был на i-ом уроке.
#
# Формат выходных данных
# Программа должна вывести фамилии учеников, которые были на всех уроках, отсортированных в лексикографическом порядке.
# Каждая фамилия должна быть записана на отдельной строке.
#
# Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
#
# Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.

m = int(input())
my_set_1 = set()

for i in range(m):
    n = int(input())
    my_set_2 = {(input()) for _ in range(n)}
    if i == 0:
        my_set_1 = my_set_2.copy()
        continue

    my_set_1.intersection_update(my_set_2)

print(*sorted(my_set_1), sep='\n')