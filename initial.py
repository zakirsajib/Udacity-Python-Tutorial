import turtle

# turtle object to initialize screen or canvas and set background color
def draw_art():
	window =turtle.Screen()
	window.bgcolor("white")


def draw_initial():
    x = turtle.Turtle()
    x.shape("turtle")
    x.color("blue")
    x.speed(3)

    #Z
    x.pu()
    x.setpos(-150,150)
    x.pd()
    x.seth(0)

    x.forward(120)
    x.right(120)
    x.forward(240)
    x.left(120)
    x.forward(120)


    #A
    x.pu()
    x.setpos(150,150)
    x.pd()
    x.seth(0)

    x.right(120)
    x.forward(240)
    x.backward(120)
    x.left(120)
    x.forward(120)
    x.left(120)
    x.forward(120)
    x.backward(240)


# Exit
def draw_exit():
	window =turtle.Screen()
	window.exitonclick()



draw_art()
draw_initial()
draw_exit()
