# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. У руководителя школы есть списки изучающих каждый предмет.
#
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.
#
# Формат входных данных
# На вход программе в первых двух строках подаются числа
# �
# m и n – количества учеников, изучающих математику и информатику соответственно.
# Далее идут m строк — фамилии учеников, которые изучают математику
# и n строк с фамилиями учеников, изучающих информатику.
#
# Формат выходных данных
# Программа должна вывести количество учеников, которые изучают только один предмет.
# Если таких учеников не окажется, то необходимо вывести NO.
#
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m = int(input())
n = int(input())

mathematics = {(input()) for _ in range(m)}
informatics = {(input()) for _ in range(n)}
only_one_item = mathematics.symmetric_difference(informatics)

if len(only_one_item) > 0:
    print(len(only_one_item))
else:
    print('NO')
