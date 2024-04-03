# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
#
# Формат входных данных
# На вход программе подаются натуральное число n≥1, а затем n различных натуральных чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.

n = int(input())
nums_ls = list()
result_set = set()
temp_set = set()

for i in range(n):
    str_num = input()
    nums_ls.append(str_num)
    if i == 0:
        for j in range(len(str_num)):
            result_set.update(str_num[j])

for i in range(1, len(nums_ls)):
    for j in range(len(nums_ls[i])):
        temp_set.update(nums_ls[i][j])
    result_set.intersection_update(temp_set)
    temp_set.clear()

result_set = sorted(result_set)
print(*result_set)