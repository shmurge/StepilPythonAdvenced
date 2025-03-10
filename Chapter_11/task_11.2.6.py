# В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik,
# проник опасный вирус и сломал контроль прав доступа к файлам.
# Говорят, вирус написал один из студентов курса Python для начинающих.

# Для каждого файла известно, с какими действиями можно к нему обращаться:

# запись W (write, доступ на запись в файл);
# чтение R (read, доступ на чтение из файла);
# запуск X (execute, запуск на исполнение файла).

# Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна
# будет возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.

# Формат входных данных
# Программа получает на вход количество файлов n, содержащихся в файловой системе компьютера.
# Далее идет n строк, на каждой имя файла и допустимые с ним операции, разделенные символом пробела.

# В следующей строке записано число m — количество запросов к файлам, и затем m строк с запросами вида операция файл.
# Одному и тому же файлу может быть адресовано любое количество запросов.

# Формат выходных данных
# Программа должна вывести для каждого из m запросов в отдельной строке Access denied или OK.

actions = {'write': 'W',
           'read': 'R',
           'execute': 'X'}

files_ls = list()
n = int(input())

for _ in range(n):
    files_ls.append(input())

m = int(input())

for _ in range(m):
    request = input().split()
    action, file_name = request[0], request[1]
    action = actions[action]

    for file in files_ls:
        if file_name in file:
            file_name = file
            break

    if action in file_name:
        print('OK')
    else:
        print('Access denied')