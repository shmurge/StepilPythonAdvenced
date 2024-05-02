# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (маленькая и большая буквы);
# «0» (цифра).

#Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре.

# Формат входных данных
# На вход программе подаются два числа n и m, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести n паролей длиной m символов в соответствии с условием задачи, каждый на отдельной строке.

# Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать возможно.

# Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре.

# Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:

# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.


from random import *
from string import *


def generate_password(length):
    simbols = [i for i in ascii_letters+digits if i not in 'lIoO10']
    password = list()
    flag = False

    while not flag:
        password = sample(simbols, length)
        password = ''.join(password)
        if (not password.isupper()) and (not password.islower()) and (not password.isdigit()) and (any(char.isdigit() for char in password)):
            flag = True
            break
        else:
            continue

    return password


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n = int(input())
m = int(input())

generate_passwords(n, m)
