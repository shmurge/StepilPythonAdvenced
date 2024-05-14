# Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов
# (любая непустая строка) по образцу: <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы).
# Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.

# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
# Примечание 2. Числа, списки, кортежи, словари, множества и другие нестроковые объекты продуктами не являются и их нужно игнорировать.
# Примечание 4. Обратите внимание: функция print_products() должна выводить (печатать) нужное значение, а не возвращать его.
# Примечание 5. Вызывать функцию print_products() не нужно, требуется только реализовать.


def print_products(*args):
    count = 1

    for arg in args:
        if type(arg) == str and str(arg).isalnum():
            print(str(count)+')', arg)
            count += 1

    if count == 1:
        print('Нет продуктов')


print_products([4], {}, 1, 2, {'Beegeek'}, '')
