# Вам доступен текстовый файл words.txt со словами, разделенными пробелом.
# Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки, не меняя их порядка следования.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Словом считайте любую группу символов без пробелов, даже если она включает цифры или знаки препинания.
# Примечание 3. Если бы файл words.txt содержал строки:

# there are many different holidays on the first of january we celebrate new year on the seventh of january and the
# twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the motherland
# or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may is victory day the
# third of july is independence day then comes the seventh of november the day of the october revolution and so on

# то результатом будет:

# twenty-fifth
# twenty-third
# independence

def long_word(file_name):
    with open(file_name) as input_file:
        original_ls = input_file.readline().split()
        max_length = max(len(word) for word in original_ls)
        result_ls = [word for word in original_ls if len(word) == max_length]
        return result_ls


print(*long_word('words.txt'), sep='\n')
