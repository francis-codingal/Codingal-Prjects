import turtle

window = turtle.Screen()
window.bgcolor("orange")
window.setup(300, 400)

painter = turtle.Turtle()

edges = 6
dist = 70
rotation = 360.0 / edges

for _ in range(edges):
    painter.forward(dist)
    painter.right(rotation)
    
turtle.done()