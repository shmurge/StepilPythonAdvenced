# Напишите программу, которая рисует соты.
# Подсказка. Убедись, что функция рисования шестиугольника возвращает черепашку в исходную точку.

import turtle


def sota(side):
    angle = 0

    for _ in range(6):
        turtle.setheading(angle)
        turtle.forward(side)
        turtle.right(60)

        for _ in range(6):
            turtle.forward(side)
            turtle.left(60)

        angle += 60


sota(50)