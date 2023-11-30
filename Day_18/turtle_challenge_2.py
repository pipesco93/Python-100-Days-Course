from turtle import  Turtle, Screen


turtle2 = Turtle()
turtle2.shape("turtle")
turtle2.color("red")

for _ in range(20): # Pn control to draw or not 
    turtle2.forward(5)
    turtle2.penup()
    turtle2.forward(5)
    turtle2.pendown()


screen = Screen()
screen.exitonclick()