# import colorgram

# rgb = []
# colors = colorgram.extract('spot.jpg', 25)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r,g,b))
#
# print (rgb)

import turtle as tur
import random as r

tur.colormode(255)
tim = tur.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(231, 234, 240), (235, 232, 225), (239, 230, 236), (226, 236, 231), (202, 163, 98), (45, 97, 147),
              (168, 49, 80),
              (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105),
              (223, 78, 56),
              (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186),
              (47, 186, 197),
              (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    tim.dot(20, r.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = tur.Screen()
screen.exitonclick()
