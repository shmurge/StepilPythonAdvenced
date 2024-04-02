# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая выводит все числа в порядке возрастания,
# которые есть как в первой строке, так и во второй.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести на одной строке через пробел числа, встречающиеся в обеих строках.

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
myset3 = sorted(myset1.intersection(myset2))

print(*myset3)