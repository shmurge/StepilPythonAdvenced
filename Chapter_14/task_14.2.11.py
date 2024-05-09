# Напишите программу, которая рисует звезду, показанную на рисунке. Такую звезду можно создать из двух треугольников.
# Однако их невозможно нарисовать непрерывной линией, поэтому перо нужно будет поднять для перехода ко второму треугольнику.

import turtle


def david_star(side):
    angle = 0

    for _ in range(3):
        turtle.setheading(angle)
        turtle.forward(side)
        angle += 120

    turtle.penup()
    position = turtle.pos()
    turtle.goto(position[0], position[1] + (side/2)+5)
    turtle.pendown()

    for _ in range(3):
        turtle.setheading(angle)
        turtle.forward(side)
        angle -= 120


david_star(100)