# Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент
# и возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным) и False
# в противном случае.


is_non_negative_num = lambda x: True if str(x).count('.') <= 1 and x.replace('.', '').isdigit() else False

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))