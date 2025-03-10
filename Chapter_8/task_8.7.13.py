# Даны по 10-балльной шкале оценки по биологии трех учеников.
# Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела
# (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами,
# в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

nums_set_1 = set(input().split())
nums_set_2 = set(input().split())
nums_set_3 = set(input().split())
ls_1 = [str(i) for i in range(11)]
result_set = set(ls_1)
result_set = result_set.difference(nums_set_1, nums_set_2, nums_set_3)
ls_2 = list(result_set)

for i in range(len(ls_2)):
    ls_2[i] = int(ls_2[i])

result_set = set(ls_2)
print(*sorted(result_set))
