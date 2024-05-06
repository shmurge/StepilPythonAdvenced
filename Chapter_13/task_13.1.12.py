# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

from decimal import Decimal as D

num = D(input())
new_tuple = num.as_tuple()
mn = None
mx = None

if '0' in str(num):
    mn = 0
else:
    mn = min(new_tuple.digits)

mx = max(new_tuple.digits)

print(mn + mx)