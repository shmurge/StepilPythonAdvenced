# Даны оценки по математике трёх учеников в 10-балльной шкале.
# Напишите программу, которая выводит такие оценки, которые встречаются не более, чем у двух учеников.
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
result_set = set()
temp_set = set()

temp_set.update(nums_set_1.intersection(nums_set_2))
temp_set = nums_set_3.difference(temp_set)
result_set.update(temp_set)
temp_set.clear()
temp_set.update(nums_set_1.intersection(nums_set_3))
temp_set = nums_set_2.difference(temp_set)
result_set.update(temp_set)
temp_set.clear()
temp_set.update(nums_set_2.intersection(nums_set_3))
temp_set = nums_set_1.difference(temp_set)
result_set.update(temp_set)
ls = list(result_set)

for i in range(len(ls)):
    ls[i] = int(ls[i])

result_set = set(ls)
result_set = sorted(result_set)

print(*result_set)