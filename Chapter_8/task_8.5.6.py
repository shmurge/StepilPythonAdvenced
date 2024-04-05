# Используя генератор множеств, дополните приведенный код так, чтобы получить множество,
# содержащее уникальные слова  строки sentence длиною меньше 4 символов.
# Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом пробела.
#
# Примечание. Учтите, что знаки пунктуации не относятся к словам.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, 
save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, 
over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, 
you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered 
and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

punctuation = """'!.,-)(?:;"""
new_sentance = ""

for c in sentence:
    if c in punctuation:
        continue
    new_sentance += c.lower()

new_sentance = list(new_sentance.split())
myset1 = {c for c in new_sentance if len(c) < 4}

print(*sorted(myset1))