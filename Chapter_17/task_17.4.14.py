# Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
# Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа,
# время выхода, где время указано в 24-часовом формате.

# Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
# (не меняя порядка следования), которые были в сети не менее часа.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем output.txt в соответствии с условием задачи.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
# Примечание 2. Считайте, что каждый пользователь был только раз в системе,
# то есть в файле нет двух строк с одинаковым пользователем.

# Примечание 3. Если бы файл logfile.txt содержал строки:
# Тимур Гуев, 14:10, 15:50
# Руслан Гриценко, 12:00, 12:59
# Роман Гацалов, 09:10, 17:45
# Габолаев Георгий, 11:10, 12:10

# то файл output.txt имел бы вид:
# Тимур Гуев
# Роман Гацалов
# Габолаев Георгий


from datetime import datetime


def log_filter(input_data, output_data):
    with open(input_data) as input_file, open(output_data, 'w') as output_file:
        result_data = []
        for line in input_file:
            ls = line.strip().split(',')
            start_time = datetime.strptime(ls[1].strip(), "%H:%M")
            end_time = datetime.strptime(ls[2].strip(), "%H:%M")
            start_minutes = start_time.hour * 60 + start_time.minute
            end_minutes = end_time.hour * 60 + end_time.minute
            diff_minutes = end_minutes - start_minutes
            if diff_minutes >= 60:
                data = ls[0] + '\n'
                result_data.append(data)

        result_data[-1] = result_data[-1][:-1]
        output_file.writelines(result_data)


log_filter('logfile.txt', 'output.txt')
