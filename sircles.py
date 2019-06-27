import turtle 
import math
import random

def exit():
	global game
	game = False

def is_colision(t1, t2):
	global size
	d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) 
		+ math.pow(t1.ycor() - t2.ycor(), 2))	
	if d < size*10:
		return True
	else:
		return False

wn = turtle.Screen()
mouse = turtle.Turtle()
mouse.shape('circle')
mouse.shapesize(0.1)
mouse.speed(0)
mouse.up()

t = turtle.Turtle()

goal = turtle.Turtle()
goal.shape('circle')
goal.color('green')
goal.up()
size = 1
score = 0
inc = 0.01
wn.onclick(mouse.goto, btn = 1)
turtle.listen()
turtle.onkey(exit, 'q')

#wn.tracer(2)
game = True
goal.goto(-100, 300)
goal.color("black")
goal.write((f"Score: {score}!"), font = ("Arial", 24, "normal"))
goal.clear()
goal.color()
while game:
	size += inc
	goal.shapesize(size)
	if size >= 5 and goal.color()[0] == 'green':
		goal.color('orange')
	if size >= 10 and goal.color()[0] == 'orange':
		goal.color('red')
	if size >= 20: 
		game = False
		wn.clear()
		wn.bgcolor('black')	
		goal.home()
		goal.color('white')
		goal.write('Game over', font = ('Arial', 24, 'normal'))
		goal.color("white")
		goal.goto(0, -100)
		goal.write(f"Scores: {score}!", font = ("Arial", 24, "normal"))
	
	if is_colision(mouse, goal):
		inc += 0.01
		size = 1
		score += 1
		goal.goto(random.randint(-300, 300), 
			random.randint(-300, 300))
		t.clear()

wn.exitonclick()