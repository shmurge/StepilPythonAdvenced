# Напишите функцию generate_letter(), которая будет собирать электронное письмо в соответствии с шаблоном:

# To: <mail>
# Приветствую, <name>!
# Вам назначен экзамен, который пройдет <date>, в <time>.
# По адресу: <place>.
# Экзамен будет проводить <teacher> в кабинете <number>.
# Желаем удачи на экзамене!
# Функция должна получать на вход пять обязательных аргументов mail, name, date, time,
# place и два необязательных teacher, number и возвращать текст готового письма.
# При отсутствии аргумента teacher учителем будет Тимур Гуев, а если нет аргумента number, то кабинет будет 17.

# Примечание 1. Следующий программный код:

# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

# должен выводить:
# To: lara@yandex.ru
# Приветствую, Лариса!
# Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
# По адресу: Часова 23, корпус 2.
# Экзамен будет проводить Тимур Гуев в кабинете 17.
# Желаем удачи на экзамене!

# To: lara@yandex.ru
# Приветствую, Лариса!
# Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
# По адресу: Часова 23, корпус 2.
# Экзамен будет проводить Василь Ярошевич в кабинете 23.
# Желаем удачи на экзамене!
# Примечание 2. Вызывать функцию generate_letter() не нужно, требуется только реализовать.

def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f'To: {mail}\n' \
           f'Приветствую, {name}!\n'\
           f'Вам назначен экзамен, который пройдет {date}, в {time}.\n'\
           f'По адресу: {place}.\n'\
           f'Экзамен будет проводить {teacher} в кабинете {number}.\n' \
           f'Желаем удачи на экзамене!'


print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))