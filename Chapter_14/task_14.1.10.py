# Напишите программу, которая рисует лучи звезды, показанной на рисунке.
# Примечание. Используйте команды forward() и backward().

import turtle


def star(angle, side):

    for _ in range(6):
        turtle.forward(side)
        turtle.backward(side*2)
        turtle.forward(side)
        turtle.left(angle)


star(30, 100)
