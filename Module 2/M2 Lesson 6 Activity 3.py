import turtle

canvas = turtle.Screen()
canvas.bgcolor("light blue")
canvas.title("Geometric Spiral")

artist = turtle.Turtle()
artist.speed(0)
line_length = 10

while line_length < 200:
    for _ in range(4):
        artist.forward(line_length)
        artist.left(90)
        line_length += 5
    line_length += 1

turtle.done()