import turtle

sides = int(input("Enter number of sides: "))
length = int(input("Enter length of each side: "))

angle = 360 / sides

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3)

for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()
