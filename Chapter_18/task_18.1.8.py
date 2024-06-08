# При написании собственных функций рекомендуется в комментарии описывать назначение функции,
# ее параметры и возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок,
# а потом и вовсе забывают о них 😂.
#
# На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python.
# Напишите программу, выводящую на экран имена всех функций, для которых отсутствует поясняющий комментарий.
# Будем считать, что любая строка, начинающаяся со слова def и пробела, является началом определения функции.
# Функция содержит комментарий, если первый символ предыдущей строки - #.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.
#
# Формат выходных данных
# Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле),
# каждое на отдельной строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют
# поясняющий комментарий, то следует вывести: Best Programming Team.

original_ls = []
result_ls = []
with open('code.txt') as input_file:
    for line in input_file:
        s = line.strip()
        original_ls.append(s)

for i in range(len(original_ls)):
    if original_ls[i - 1] != '' and original_ls[i - 1][0] == '#':
        continue
    ls = original_ls[i].split()
    for j in range(len(ls)):
        if ls[j] == 'def':
            s = ls[j + 1]
            index = s.index('(')
            result_ls.append(s[:index])

if len(result_ls) == 0:
    result_ls.append('Best Programming Team')

print(*result_ls, sep='\n')
