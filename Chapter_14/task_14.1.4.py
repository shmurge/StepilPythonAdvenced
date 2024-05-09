# Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.

# Примечание 1. Напишите функцию square(side), где side – длина стороны квадрата в пикселях.

# Примечание 2. Поэксперементируйте с углом поворота черепашки при переходе от одного квадрата к другому.

from time import sleep
import turtle


def square(side):
    angle = 0

    for _ in range(3):
        angle += 25
        turtle.setheading(angle)
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)


square(150)
