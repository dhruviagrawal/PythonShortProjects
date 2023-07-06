from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)


# color = ["cyan", "CornflowerBlue", "DarkOrchid", "IndianRed", "wheat", "SlateGray", "SeaGreen", "CornFlowerBlue",
#          "DeepSkyBlue"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]

# tim.pensize(10)
tim.speed("fastest")
r = 100


def spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.circle(r)
        current_heading = tim.heading()
        tim.setheading(current_heading + gap_size)
        # tim.forward(30)
        # tim.setheading(random.choice(directions))
        tim.color(random_color())


spirograph(5)

screen = Screen()
screen.exitonclick()
