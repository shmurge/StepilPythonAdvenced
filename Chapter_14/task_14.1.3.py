# Напишите программу, которая рисует правильный треугольник.
# Примечание 1. Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.
#
# Примечание 2. Величина каждого угла правильного треугольника равна 60 градусам.

from time import sleep
import turtle


def triangle(side):
    angle = 120

    for i in range(3):
        turtle.forward(side)
        turtle.left(angle)


triangle(100)
