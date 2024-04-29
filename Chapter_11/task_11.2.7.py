# Напишите программу для подсчета количества единиц каждого вида товара из
# приобретенных каждым покупателем интернет-магазина.
#
# Формат входных данных
# На вход программе подается число n — количество строк в базе данных о продажах интернет-магазина.
# Далее следует n строк с записями вида покупатель товар количество,
# где покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара (натуральное число).
#
# Формат выходных данных
# Программа должна вывести список всех покупателей в лексикографическом порядке,
# после имени каждого покупателя — двоеточие, затем список названий всех приобретенных им товаров
# в лексикографическом порядке, после названия каждого товара — количество единиц товара.
# Информация о каждом товаре выводится на отдельной строке.
#
# Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает
# суммарное количество товара по данной позиции.

user_products = dict()
n = int(input())

for _ in range(n):
    data = input().split()
    user_name = data[0]
    position = data[1]
    quantity = int(data[2])
    if user_name not in user_products:
        user_products[user_name] = {position: quantity}
    else:
        if position in user_products[user_name]:
            user_products[user_name][position] += quantity
        else:
            user_products[user_name][position] = quantity

for key, value in sorted(user_products.items()):
    print(key+':')
    for k, v in sorted(value.items()):
        print(k, v)
