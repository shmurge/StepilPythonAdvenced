# На вход программе подаются две строки текста, содержащие числа. Напишите программу,
# которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести множество чисел, встречающихся только в первой строке.

def str_in_nums(initial_list):
    new_list = list()
    for i in range(len(initial_list)):
        new_list.append(int(initial_list[i]))
    return new_list


str_ls1 = input().split()
str_ls2 = input().split()
num_ls1 = str_in_nums(str_ls1)
num_ls2 = str_in_nums(str_ls2)

myset1 = set(num_ls1)
myset2 = set(num_ls2)
myset3 = sorted(myset1.difference(myset2))

print(*myset3)

