# Напишите программу, которая случайным образом назначает каждому ученику его тайного друга,
# который будет вместе с ним решать задачи по программированию.

# Формат входных данных
# На вход программе в первой строке подается число n – общее количество учеников.
# Далее идут n строк, содержащих имена и фамилии учеников.

# Формат выходных данных
# Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного друга,
# разделённые дефисом.
#
# Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для нескольких учеников.
#
# Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных друзей.

from random import *


def secret_friend(quantity):
    students_ls = [input() for _ in range(quantity)]
    secret_friend_ls = list()
    result_ls = list()

    for i in range(len(students_ls)):
        student = students_ls[i]

        while 1 == 1:
            friend = choice(students_ls)
            if (friend != student) and (friend not in secret_friend_ls):
                row = student + ' - ' + friend
                result_ls.append(row)
                secret_friend_ls.append(friend)
                break

    return result_ls


n = int(input())
print(*secret_friend(n), sep='\n')

