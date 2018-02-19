import turtle

# turtle object to initialize screen or canvas and set background color
def draw_art():
	window =turtle.Screen()
	window.bgcolor("red")


# first turtle object to create a square
def draw_square():
	turtle_name = turtle.Turtle()
	turtle_name.shape("circle")
	turtle_name.color("green")
	turtle_name.speed(3)

	for i in range(0,4):
		turtle_name.forward(100)
		turtle_name.right(90)


# Another turtle object to create a circle
def draw_circle():
	turtle_name2 = turtle.Turtle()
	turtle_name2.shape("arrow")
	turtle_name2.color("blue")
	turtle_name2.speed(3)
	turtle_name2.circle(100)

# Another turtle object to create a triangle
def draw_triangle():
	turtle_name3 = turtle.Turtle()
	turtle_name3.shape("triangle")
	turtle_name3.color("black")
	turtle_name3.speed(3)

	for i in range(0,3):
		turtle_name3.forward(100)
		turtle_name3.right(120)


# Exit
def draw_exit():
	window =turtle.Screen()
	window.exitonclick()


draw_art()
draw_square()
draw_circle()
draw_triangle()
draw_exit()
