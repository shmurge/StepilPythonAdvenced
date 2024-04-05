# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
#
# Формат входных данных
# На вход программе подаются натуральное число n≥1, а затем n различных натуральных чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.

n = int(input())
ls_1 = [str(i) for i in range(11)]
result_set = set(ls_1)

for i in range(n):
    result_set.intersection_update(input())

ls_2 = list(result_set)

for i in range(len(ls_2)):
    ls_2[i] = int(ls_2[i])

result_set = set(ls_2)

print(*sorted(result_set))