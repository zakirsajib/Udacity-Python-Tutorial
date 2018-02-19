# Making a circle out of triangles

import turtle

# turtle object to initialize screen or canvas and set background color
def draw_art():
	window =turtle.Screen()
	window.bgcolor("white")


# first turtle object to create a triangle
def draw_triangle(x):
	for i in range(0,3):
		x.forward(200)
		x.right(120)

# Creating a sun using triangle
def draw_sun_using_triangle():
	x = turtle.Turtle()
	x.shape("turtle")
	x.color("blue")
	x.speed(3)
	for i in range(0,38):
		draw_triangle(x)
		x.right(10)


# Exit
def draw_exit():
	window =turtle.Screen()
	window.exitonclick()


draw_art()
draw_sun_using_triangle()
draw_exit()
