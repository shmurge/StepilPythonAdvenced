# Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу,
# которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела
# (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке убывания на одной строке,
# разделенных пробелами, в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

nums_set_1 = set(input().split())
nums_set_2 = set(input().split())
nums_set_3 = set(input().split())
result_set = nums_set_3.difference(nums_set_1, nums_set_2)
ls = list(result_set)

for i in range(len(ls)):
    ls[i] = int(ls[i])

result_set = set(ls)
print(*sorted(result_set, reverse=True))
