# Programming Assignment 4
# Mike Nguyen
# 1249432


from turtle import Screen, Turtle


def square(turtle, x, y, length):
    tx = x + length / 2
    ty = y + length / 2

    turtle.penup()
    turtle.setx(tx)
    turtle.sety(ty)
    turtle.pendown()

    drawSquare(turtle, tx, ty, length)

    return


def drawSquare(turtle, tx, ty, length):
    turtle.begin_fill()

    turtle.goto(tx, ty - length)
    turtle.goto(tx - length, ty - length)
    turtle.goto(tx - length, ty)
    turtle.goto(tx, ty)

    turtle.end_fill()
    return


def pattern(iteration, turtle, x, y, length):
    if iteration == 0:
        return

    square(turtle, x, y, length)

    ratio = 2.2

    pattern(iteration - 1, turtle, x - (length / 2), y - (length / 2), length / ratio)
    pattern(iteration - 1, turtle, x - (length / 2), y + (length / 2), length / ratio)
    pattern(iteration - 1, turtle, x + (length / 2), y - (length / 2), length / ratio)
    pattern(iteration - 1, turtle, x + (length / 2), y + (length / 2), length / ratio)
    return


s = Screen()
t = Turtle()

t.color("red")
pattern(4, t, 0, 0, 300)

s.exitonclick()
