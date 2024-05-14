# Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).

# Напишите программу сортировки списка спортсменов по указанному полю:

# 1: по имени;
# 2: по возрасту;
# 3: по росту;
# 4: по весу.

# Формат входных данных
# На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.

# Формат выходных данных
# Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.

# Примечание. Решите задачу без использования условного оператора.


def compare_by_name(collection):
    return collection[0]


def compare_by_age(collection):
    return collection[1]


def compare_by_height(collection):
    return collection[2]


def compare_by_weight(collection):
    return collection[3]


funcs = [compare_by_name, compare_by_age, compare_by_height, compare_by_weight]
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

i = int(input()) - 1

sorted_athletes = sorted(athletes, key=funcs[i])

for athlete in sorted_athletes:
    print(*athlete)