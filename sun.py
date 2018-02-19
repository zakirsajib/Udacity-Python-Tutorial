#Making a circle out of squares

import turtle

# turtle object to initialize screen or canvas and set background color
def draw_art():
	window =turtle.Screen()
	window.bgcolor("red")


# first turtle object to create a square
def draw_square(x):
	for i in range(0,4):
		x.forward(100)
		x.right(90)


def draw_sun_using_square():
	x = turtle.Turtle()
	x.shape("circle")
	x.color("green")
	x.speed(3)
	for i in range(0,38):
		draw_square(x)
		x.right(10)


# Exit
def draw_exit():
	window =turtle.Screen()
	window.exitonclick()


draw_art()
draw_sun_using_square()
draw_exit()
