import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

r = 100
tim.speed("fastest")

def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(random_color())
        tim.circle(r)
        tim.setheading( tim.heading() + size_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()