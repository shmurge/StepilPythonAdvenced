# Формат входных данных
# В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки
# (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.
#
# Формат выходных данных
# Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.
#
# Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.

number_of_points = int(input())
list_of_points = []
first = "Первая четверть: "
second = "Вторая четверть: "
third = "Третья четверть: "
fourth = "Четвертая четверть: "
fst_count = 0
scd_count = 0
thd_count = 0
fth_count = 0

for i in range(number_of_points):
    points = input()
    ls_1 = points.split()
    list_of_points.append(ls_1)

for i in range(len(list_of_points)):
    ls_2 = list_of_points[i]
    x = int(ls_2[0])
    y = int(ls_2[1])
    if x > 0 and y > 0:
        fst_count += 1
    elif x < 0 and y > 0:
        scd_count += 1
    elif x < 0 and y < 0:
        thd_count += 1
    elif x > 0 and y < 0:
        fth_count += 1

print(first, fst_count)
print(second, scd_count)
print(third, thd_count)
print(fourth, fth_count)

