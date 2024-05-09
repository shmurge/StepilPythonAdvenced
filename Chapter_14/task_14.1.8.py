# Напишите программу, которая рисует ромб с углами 60 и 120 градусов.

import turtle


def rhombus(angle1, angle2, side):

    for _ in range(2):
        turtle.forward(side)
        turtle.left(angle2)
        turtle.forward(side)
        turtle.left(angle1)


rhombus(60, 120, 100)