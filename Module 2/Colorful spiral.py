import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "magenta", "blue", "cyan", "green", "yellow"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i * 1.5)
    t.left(61)
    t.width(i / 100 + 1)

turtle.done()
