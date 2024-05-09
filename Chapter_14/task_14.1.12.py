# Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.

import turtle


def square_pattern(side):

    for _ in range(20):
        turtle.setheading(90)

        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

        side += 10


square_pattern(50)