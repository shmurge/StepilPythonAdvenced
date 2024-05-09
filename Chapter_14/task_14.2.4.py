# Напишите программу для рисования паутины в соответствии с примером.
# Программа должна считывать количество лучей паутины, число n.
#
# Примечание. Угол заданный каждой парой лучей составляет 360/n градусов.

import turtle


def web(side, num_of_rays):
    angle = 360/num_of_rays
    turtle.dot()

    for _ in range(num_of_rays):
        turtle.forward(side)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(side)
        turtle.right(180)
        turtle.left(angle)


web(100, 7)
