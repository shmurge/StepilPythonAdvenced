# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
#
# Формат входных данных
# На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк со словами.
#
# Формат выходных данных
# Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.

n = int(input())
my_set = set()

for i in range(n):
    my_set.update(input().lower())

print(len(my_set))

