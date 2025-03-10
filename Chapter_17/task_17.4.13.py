# На вход программе подается натуральное число n и n строк с названиями файлов. Напишите программу,
# которая создает файл output.txt и выводит в него содержимое всех файлов, не меняя их порядка.
# Смотрите Примечание 2 для понимания работы программы.

# Формат входных данных
# На вход программе подается натуральное число n и n строк названий существующих файлов.

# Формат выходных данных
# Программа должна создать файл с именем output.txt в соответствии с условием задачи.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
#
# Примечание 2. Если бы на вход было подано 2 файла и эти файлы содержали бы строки (обратите внимание,
# что в конце первого файла нет переноса строки)

# Early in the morning
# и
# we
# went
# for mushrooms
# то результирующий файл output.txt выглядел бы следующим образом:

# Early in the morningwe
# went
# for mushrooms


def files_concatenate(quantity):
    for _ in range(quantity):
        file_name = input()
        with open(file_name) as input_file, open('output.txt', 'a') as output_file:
            content = input_file.readlines()
            output_file.writelines(content)


files_concatenate(int(input()))


