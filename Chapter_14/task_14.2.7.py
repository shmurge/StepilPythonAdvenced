# Напишите программу, которая рисует черепашью спираль в соответствии с образцом.

import turtle


def turtle_spiral(quantity):
    side = 0
    angle = 0
    turtle.shape('turtle')
    turtle.penup()

    for _ in range(quantity):
        turtle.forward(side)
        turtle.setheading(angle)
        turtle.stamp()
        side += 1
        angle -= 20


turtle_spiral(50)