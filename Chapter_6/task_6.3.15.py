# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Трибоначчи.

# Формат входных данных
# На вход программе подается одно число n (n≤100) – количество членов последовательности.

# Формат выходных данных
# Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.

# Примечание. Последовательность Трибоначчи – последовательность натуральных чисел,
# где каждое последующее число является суммой трех предыдущих

n = int(input())
num1, num2, num3 = 1, 1, 1

for _ in range(n):
    print(num1, end=" ")
    num1, num2, num3 = num2, num3, num1+num2+num3
