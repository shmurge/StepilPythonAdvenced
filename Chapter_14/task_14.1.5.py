# Напишите программу, которая рисует изображенную фигуру из восьми квадратов.
# Примечание. Используйте функцию square(side) из предыдущей задачи.

from time import sleep
import turtle


def square(side):
    angle = 0

    for _ in range(8):

        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

        angle += 45
        turtle.setheading(angle)


square(150)