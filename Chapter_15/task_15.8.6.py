# Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
# значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен)
# и False в противном случае.


func = lambda x: True if x[0].lower() == 'a' and x[-1].lower() == 'a' else False

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))