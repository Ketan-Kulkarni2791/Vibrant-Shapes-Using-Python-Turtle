import turtle

turtle.bgcolor('Black')
turtle.pensize(2)


def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.speed(0)
turtle.color("red", "pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
style = ('Courier', 20, 'bold')
turtle.write("Love You Aasawari !", font=style, align='center')
turtle.hideturtle()
turtle.done()
