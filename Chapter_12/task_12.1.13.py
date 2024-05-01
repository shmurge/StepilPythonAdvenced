# Напишите программу, которая с помощью модуля random генерирует случайный пароль.
# Программа принимает на вход длину пароля и выводит случайный пароль,
# содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
#
# Примечание 1. Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.
#
# Примечание 2. Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.
#
# Примечание 3. Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.
#
#  Примечание 4. Например, при длине пароля, равной 15 символам, ваша программа может выводить: peJFAmhqfaAeKDu

import random

length = int(input())    # длина пароля


def pass_generator(pass_length):
    password = list()

    while len(password) != length:
        password.append(chr(random.randint(65, 122)))
        for i in range(91, 97):
            if chr(i) in password:
                del password[-1]

    random.shuffle(password)
    password = "".join(password)

    return password

print(pass_generator(length))

