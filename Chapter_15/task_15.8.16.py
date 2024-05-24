# Значение многочлена 🌶️

from functools import *


def evaluate(coefficients, x):
    indexes = [i for i in range(len(coefficients))]
    indexes.sort(reverse=True)
    x_ls = [x for i in range(len(coefficients))]
    total = sum(list(map(summ, coefficients, x_ls, indexes)))
    return total


def summ(elem1, elem2, degree):
    return elem1*elem2**degree


nums_list = [int(num) for num in input().split()]
x = int(input())
print(evaluate(nums_list, x))