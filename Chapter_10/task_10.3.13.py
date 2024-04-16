# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s.
# Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
    'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate ' \
    'barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot ' \
    'currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant ' \
    'orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

ls = s.split()
dict1 = {}
result = {}

for word in ls:
    if word not in dict1:
        dict1[word] = 1
    else:
        dict1[word] += 1

max_count = (max(dict1.values()))

for v in dict1:
    if dict1[v] == max_count:
        result[v] = dict1[v]

print(min(result))
