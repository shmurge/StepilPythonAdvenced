# Напишите программу, которая рисует пунктирную линию

# Примечание. Поэкспериментируйте с формой черепашки.

import turtle


def dotted_line(side):
    turtle.forward(side)
    turtle.penup()
    turtle.forward(side)
    turtle.pendown()


for _ in range(5):
    dotted_line(5)