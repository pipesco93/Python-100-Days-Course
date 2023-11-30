from operator import ipow
from turtle import  Turtle, Screen
import random


turtle3 = Turtle()

def draw_shape(number_of_sides):
    for _ in range(number_of_sides):

        angle = 360/number_of_sides
        turtle3.forward(100)
        turtle3.right(angle)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


number_of_sides = 3

for shape_side in range(10):

    draw_shape(number_of_sides)
    turtle3.color(random.choice(colours))
    number_of_sides += 1


screen = Screen()
screen.exitonclick()