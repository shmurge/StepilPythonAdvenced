# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
# далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и
# далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

# Напишите программу создания файла answer.txt и вывода в него списка козлов,
# которые удовлетворяют условию загадки от Жака Фреско.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов,
# которые удовлетворяют условию загадки Жака Фреско.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
# Примечание 2. Если бы файл goats.txt содержал строки:

# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Black goat
# Pink goat

# то файл answer.txt имел бы вид:
#
# Black goat
# Pink goat


def jacques_fresco(original_file, result_file):
    original_list = list()
    updated_list = list()
    result_list = list()
    total = 0
    colours_dict = {}

    with open(original_file) as input_file:
        for line in input_file:
            s = line.strip()
            if s == 'COLOURS':
                continue
            original_list.append(s)

    for line in original_list:

        if line == 'GOATS':
            index = original_list.index('GOATS')
            updated_list = original_list[index+1:]
            break
        colours_dict[line] = 0

    with open(result_file, 'a') as output_file:
        for line in updated_list:
            colours_dict[line] += 1
            total += 1
        for key, value in colours_dict.items():
            if ((value * 100) / total) > 7:
                result_list.append(key+'\n')
        result_list[-1] = result_list[-1][:-1]
        result_list.sort()
        output_file.writelines(result_list)


jacques_fresco('goats.txt', 'answer.txt')

