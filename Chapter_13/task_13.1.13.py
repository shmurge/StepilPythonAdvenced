# На вход программе подается Decimal число d.
# Напишите программу, которая вычисляет значение выражения: e^d + ln(d) + lg(d) + sqrt(d)

# Формат входных данных
# На вход программе подается положительное десятичное число d.

# Формат выходных данных
# Программа должна вывести искомое значение выражения.

from decimal import Decimal as D

d = D(input())
result = d.exp() + d.ln() + d.log10() + d.sqrt()

print(result)