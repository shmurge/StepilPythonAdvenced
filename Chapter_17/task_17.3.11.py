# Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все что угодно.
# Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

# Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести сумму всех чисел, записанных в файле.

with open('nums.txt') as file:
    original_list = [i.strip('\n') for i in file.readlines()]
    context = list()
    num = ''
    for line in original_list:

        for ch in line:
            if ch.isdigit():
                num += ch
            else:
                if num != '':
                    context.append(int(num))
                    num = ''
                continue

        if num != '':
            context.append(int(num))
            num = ''

    print(sum(context))
