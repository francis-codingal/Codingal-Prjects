import turtle

workspace = turtle.Screen()
brush = turtle.Turtle()

side_unit = 100

for _ in range(4):
    brush.forward(side_unit)
    brush.left(90)

turtle.done()