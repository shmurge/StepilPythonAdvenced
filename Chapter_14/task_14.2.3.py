# Напишите программу, которая рисует прямоугольник с точкой в каждом углу

import turtle


def rectangle_with_dot(width, height):

    for i in range(2):
        turtle.dot()
        turtle.forward(width)
        turtle.right(90)

        turtle.dot()
        turtle.forward(height)
        turtle.right(90)


rectangle_with_dot(100, 50)
