# Напишите программу, которая рисует правильную пятиконечную звезду.
# Примечание. Используйте угол поворота в 144∘.

import turtle


def five_pointed_star(angle, side):

    for _ in range(5):
        turtle.setheading(angle)
        turtle.forward(side)
        angle += 144


five_pointed_star(180, 150)