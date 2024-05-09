# Напишите программу, которая рисует прямоугольник.
# Примечание. Программу нужно оформить в виде функции rectangle(width, height),
# где width, height – ширина и высота прямоугольника.

import turtle


def rectangle(width, height):

    for i in range(2):
        turtle.forward(width)
        turtle.right(90)

        turtle.forward(height)
        turtle.right(90)


rectangle(300, 100)
