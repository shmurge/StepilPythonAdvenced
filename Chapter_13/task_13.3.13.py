# Комплексные числа хранятся в списке numbers. Дополните приведенный код так,
# чтобы он вывел комплексное число с наибольшим модулем и сам модуль числа на отдельных строках.

# Примечание. Модуль комплексного числа можно вычислить с помощью встроенной функции abs().


numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1
           - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
max_cnum = complex()
max_abc_cnum = 0

for num in numbers:
    if abs(num) > max_abc_cnum:
        max_cnum = complex(num)
        max_abc_cnum = abs(num)

print(max_cnum, max_abc_cnum, sep='\n')