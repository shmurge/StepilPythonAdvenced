# Напишите программу, которая рисует узор в соответствии с образцом.

import turtle


def color_spiral(list_of_colors):
    side = 1
    size = 1
    angle = 0
    color = 0

    while side != 101:
        if color == len(list_of_colors):
            color = 0
        turtle.pencolor(colors[color])
        turtle.pensize(size)
        turtle.setheading(angle)
        turtle.forward(side)
        side += 1
        size += 0.05
        angle -= 45
        color += 1


colors = ['yellow', 'blue', 'red', 'orange', 'violet', 'green']

color_spiral(colors)