# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).
#
# Напишите функцию generate_index(), которая с помощью модуля random генерирует
# и возвращает случайный корректный почтовый индекс Латверии.
#
# Примечание 1. Пример правильного (неправильного) индекса Латверии:
#
# AB23_56VG          # правильный
# V3F_231GT          # неправильный

# Примечание 2. Обратите внимание на символ _ в почтовом индексе.
#
# Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.

import string
import random


def generate_index():
    letters = string.ascii_uppercase
    digits = string.digits
    index = list()
    index.append(random.sample(letters, 2) + random.sample(digits, 2)
                 + ['_'] + random.sample(digits, 2) + random.sample(letters, 2))
    index = index[0]
    index = ''.join(index)

    return index

print(generate_index())