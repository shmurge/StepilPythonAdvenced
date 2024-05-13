# Напишите программу, которая рисует изображение символа олимпиады в соответствии с образцом.

import turtle

r = 50
pensize = 6
turtle.Screen().setup(600, 1000)
turtle.pensize(pensize)

points = {1: {"pos": (0, 0), "color": "cyan"},
          3: {"pos": (r * 2, 0), "color": "black"},
          4: {"pos": (r * 4, 0), "color": "red"},
          5: {"pos": (r, -r), "color": "yellow"},
          2: {"pos": (r * 3, -r), "color": "chartreuse"}}

for i in range(1, 6):
    turtle.penup()
    turtle.pencolor(points[i]["color"])
    turtle.goto(points[i]["pos"])
    turtle.pendown()
    turtle.circle(r - pensize / 2)
