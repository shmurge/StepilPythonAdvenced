# Сопряжение числа. Условия смотреть тут:
# https://stepik.org/lesson/360942/step/14?auth=login&unit=345465

from cmath import *


n = int(input())
z1 = complex(input())
z2 = complex(input())

print(z1**n + z2**n + (z1.conjugate()**n) + (z2.conjugate()**(n+1)))
