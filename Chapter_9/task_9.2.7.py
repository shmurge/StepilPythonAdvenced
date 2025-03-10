# При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует
# не только профессиональные качества кандидата, но и его память.
#
# Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их назвать.
# Причем неважно, в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все числа,
# не добавляя лишних.
#
# Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.
#
# Формат входных данных
# На вход программе подаются две строки с числами: в первой строке показанные кандидату, а во второй ответы кандидата.
#
# Формат выходных данных
# Программа должна вывести YES, если кандидат прошел испытание и его можно брать на работу и NO в противном случае.

my_set_1 = {int(n) for n in input().split()}
my_set_2 = {int(n) for n in input().split()}

if my_set_2 <= my_set_1 and len(my_set_2) == len(my_set_1):
    print('YES')
else:
    print('NO')