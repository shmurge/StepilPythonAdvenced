# Напишите программу, которая рисует циферблат часов в соответствии с образцом.

import turtle


def turtle_clock_face(background_color):
    turtle.Screen().bgcolor(background_color)
    angle = 360 / 12
    turtle.shape('turtle')
    turtle.stamp()

    for _ in range(12):
        turtle.penup()
        turtle.forward(75)
        turtle.pendown()
        turtle.forward(15)
        turtle.penup()
        turtle.forward(10)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(100)
        turtle.right(180)
        turtle.left(angle)


turtle_clock_face('CadetBlue1')