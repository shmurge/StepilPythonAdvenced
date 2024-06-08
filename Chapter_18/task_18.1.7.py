# Транслитерация — передача знаков одной письменности знаками другой письменности,
# при которой каждый знак (или последовательность знаков) одной системы письма передаётся соответствующим знаком
# (или последовательностью знаков) другой системы письма.

# Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла,
# то есть замены кириллических символов на латинские в соответствии с предложенной таблицей.
# Все остальные символы надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt.

# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем transliteration.txt в соответствии с условием задачи.
#
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
# Примечание 2. Обратите внимание, что заглавные буквы должны заменяться на соответствующие им заглавные же буквы,
# но если транслитерационная последовательность состоит из нескольких символов, то заглавным будет только первый из них:
# «С» на «S», а «Я» на «Ya».
#
# Примечание 3. Если бы файл cyrillic.txt содержал текст:

# Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
# We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so
# hard to help him: they don’t want the truth to be exposed.

# то содержимое файла transliteration.txt будет:
#
# Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
# We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to
# help him: they don’t want the truth to be exposed.


# Таблица транслитерации
translit_table = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y',
    'ь': "'", 'э': 'je', 'ю': 'ju', 'я': 'ya'
}

# Чтение текста из файла cyrillic.txt
with open('cyrillic.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Транслитерация текста
transliterated_text = ''
for char in text:
    if char.lower() in translit_table:
        if char.isupper():
            transliterated_text += translit_table[char.lower()].capitalize()
        else:
            transliterated_text += translit_table[char.lower()]
    else:
        transliterated_text += char

# Запись результата в файл transliteration.txt
with open('transliteration.txt', 'w', encoding='utf-8') as file:
    file.write(transliterated_text)