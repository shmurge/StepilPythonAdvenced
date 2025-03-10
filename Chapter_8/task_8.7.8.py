# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
#
# Формат входных данных
# На вход программе подаются два натуральных числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.

num1 = input()
num2 = input()
my_set_1 = set()
my_set_2 = set()

for i in range(len(num1)):
    my_set_1.update(num1[i])

for i in range(len(num2)):
    my_set_2.update(num2[i])

if my_set_1.isdisjoint(my_set_2):
    print("NO")
else:
    print("YES")