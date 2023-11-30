from turtle import  Turtle, Screen

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("red")

for _ in range(4):
    turtle1.forward(100)
    turtle1.right(90)

screen = Screen()
screen.exitonclick()