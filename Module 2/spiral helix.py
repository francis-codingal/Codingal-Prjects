import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(300):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)

turtle.done()
