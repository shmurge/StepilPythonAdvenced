# Напишите программу, которая рисует узор, показанный на рисунке.

import turtle


def maze(side):
    turtle.setheading(90)
    turtle.forward(side)

    for _ in range(10):

        for _ in range(4):
            side += 10
            turtle.left(90)
            turtle.forward(side)


maze(10)
