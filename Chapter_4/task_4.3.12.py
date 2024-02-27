# На вход программе подается строка текста, содержащая символы. Напишите программу,
# которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести указанный вложенный список.

text_ls = [i for i in input().split()]
text = "".join(text_ls)
ls = list()
ls.append(text[0])
final_ls = list()

for i in range(1, len(text)):
    if text[i] in ls:
        ls.append(text[i])
        continue
    final_ls.append(ls)
    ls = [text[i]]

final_ls.append(ls)
print(final_ls)
