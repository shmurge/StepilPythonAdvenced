# Напишите программу, которая рисует черепашек в соответствии с образцом.

import turtle


def turtles(side, num_of_rays):
    angle = 360/num_of_rays
    turtle.shape('turtle')
    turtle.stamp()
    turtle.penup()

    for _ in range(num_of_rays):
        turtle.forward(side)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(side)
        turtle.right(180)
        turtle.left(angle)


turtles(100, 7)
