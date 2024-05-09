# Напишите программу, которая рисует снежинку из 10 ромбов.

import turtle


def rhombus(angle1, angle2, side):

    for _ in range(2):
        turtle.forward(side)
        turtle.left(angle2)
        turtle.forward(side)
        turtle.left(angle1)


angle = 10

for _ in range(10):
    turtle.setheading(angle)
    rhombus(120, 60, 100)
    angle += 37
