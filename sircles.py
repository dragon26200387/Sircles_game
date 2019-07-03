import turtle
import math
import random

def is_colision(t1, t2):
	global size
	d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)
		+ math.pow(t1.ycor() - t2.ycor(), 2))
	if d < size*10:
		return True
	else:
		return False

wn = turtle.Screen()
wn.bgpic("background.gif")
mouse = turtle.Turtle()
mouse.shape('circle')
mouse.shapesize(0.1)
mouse.speed(0)
mouse.up()

t = turtle.Turtle()

maxGoals = 10
goals = []
for i in range(maxGoals):
	goals.append(turtle.Turtle())
	goals[i].shape("circle")
	goals[i].color("green")
	goals[i].up()
	goals[i].goto(random.randint(-300, 300), random.randint(-300, 300))

size = 1
score = 0
inc = 0.01
wn.onclick(mouse.goto, btn = 1)
turtle.listen()

#wn.tracer(2)
game = True
goals[i].goto(-100, 300)
while game:
	size += inc
	for i in range(maxGoals):
                goals[i].shapesize(size)
                if size >= 5 and goals[i].color()[0] == 'green':
                        goals[i].color('yellow')
                if size >= 10 and goals[i].color()[0] == 'yellow':
                        goals[i].color('orange')
                if size >= 15 and goals[i].color()[0] == 'orange':
                        goals[i].color('red')
                if size >= 20: 
                        game = False
                        wn.clear()
                        wn.bgcolor('black')
                        goals[i].home()
                        goals[i].color('white')
                        goals[i].write('Game over', font = ('Arial', 24, 'normal'))
                        goals[i].color("white")
                        goals[i].goto(0, -100)
                        goals[i].write(f"Scores: {score}!", font = ("Arial", 24, "normal"))
                if is_colision(mouse, goals[i]):
                        inc += 0.01
                        size = 1
                        score += 1
                        goals[i].goto(random.randint(-300, 300),
                        random.randint(-300, 300))
                        t.clear()

wn.exitonclick()