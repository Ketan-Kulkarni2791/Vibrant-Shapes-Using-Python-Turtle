import turtle
import time
screen = turtle.Screen()
trtl = turtle.Turtle()
screen.setup(420, 320)
screen.bgcolor('black')
clrs = ['red', 'green', 'blue', 'yellow', 'purple']
trtl.pensize(4)
trtl.penup()
trtl.setpos(-90, 30)
trtl.pendown()
for i in range(5):
    trtl.pencolor(clrs[i])
    trtl.forward(200)
    trtl.right(144)
trtl.penup()
trtl.setpos(80, -140)
trtl.pendown()
trtl.pencolor('olive')
trtl.write('Pure python', font=("Arial", 12, "normal"))
trtl.ht()

