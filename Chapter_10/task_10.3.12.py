# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого символа строки text будет подсчитано количество его вхождений.
#
# Примечание. Выводить содержимое словаря result не нужно.

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for c in text:
    item = result.setdefault(c, text.count(c))
