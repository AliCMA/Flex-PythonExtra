import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("blue")
turtle.fillcolor("white")
turtle.begin_fill()

for x in range(66):
    turtle.forward(64)
    turtle.right(90)
    turtle.forward(34)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(5)

turtle.end_fill()
turtle.done()