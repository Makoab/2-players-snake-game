import turtle
import time
import random
#screen stuff
screen= turtle.Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor('black')
screen.setup(600,600)

#snakes stuff
snake1=turtle.Turtle()
snake1.shape('square')
snake1.color('white')
snake1.speed(0)
snake1.penup()
snake1.goto(-200,0)
snake1.direction='stop'

snake2=turtle.Turtle()
snake2.shape('square')
snake2.color('yellow')
snake2.speed(0)
snake2.penup()
snake2.goto(200,0)
snake2.direction='stop'

#apple stuff
apple=turtle.Turtle()
apple.shape('circle')
apple.color('red')
apple.speed(0)
apple.penup()
apple.goto(0,0)
apple.direction='stop'

# Score display setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('lightgreen')
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

def up():
	if snake1.direction!='down':
		snake1.direction='up'
def up2():
	if snake2.direction!='down':
		snake2.direction='up'
def down():
	if snake1.direction!='up':
		snake1.direction='down'
def down2():
	if snake2.direction!='up':
		snake2.direction='down'
def right():
	if snake1.direction!='left':
		snake1.direction='right'
def right2():
	if snake2.direction!='left':
		snake2.direction='right'
def left():
	if snake1.direction!='right':
		snake1.direction='left'
def left2():
	if snake2.direction!='right':
		snake2.direction='left'
# two console
screen.listen()
screen.onkeypress(up,'w')
screen.onkeypress(down,'s')
screen.onkeypress(right,'d')
screen.onkeypress(left,'a')

screen.onkeypress(up2,'Up')
screen.onkeypress(down2,'Down')
screen.onkeypress(right2,'Right')
screen.onkeypress(left2,'Left')

def move():
	if snake1.direction=='up':
		y=snake1.ycor()
		snake1.sety(y+20)
	if snake1.direction =='down':
		y = snake1.ycor()
		snake1.sety(y - 20)
	if snake1.direction =='right':
		x = snake1.xcor()
		snake1.setx(x + 20)
	if snake1.direction =='left':
		x = snake1.xcor()
		snake1.setx(x - 20)

def move2():
	if snake2.direction=='up':
		y=snake2.ycor()
		snake2.sety(y+20)
	if snake2.direction =='down':
		y = snake2.ycor()
		snake2.sety(y - 20)
	if snake2.direction =='right':
		x = snake2.xcor()
		snake2.setx(x + 20)
	if snake2.direction =='left':
		x = snake2.xcor()
		snake2.setx(x - 20)

# Function to display the winner
def display_winner(winner):
    score_display.write(f"Player {winner} Wins!", align="center", font=("Courier", 24, "normal"))
    score_display.clear()
# Function to reset the game
def reset_game(winner):
	display_winner(winner)
	time.sleep(2)# Pause for 2 seconds to show the winner
	snake1.goto(-200, 0)
	snake2.goto(200, 0)
	apple.goto(0, 0)
	snake1.direction = 'stop'
	snake2.direction = 'stop'

	for part in parts:
		part.goto(2000, 2000)
	parts.clear()

	for part2 in parts2:
		part2.goto(2000, 2000)
	parts2.clear()

# Main game loop
parts=[]
parts2=[]
while True:
	screen.update()

	# corner limit
	if snake1.xcor()>290 or snake1.xcor()<-290 or snake1.ycor()>290 or snake1.ycor()<-290:
		reset_game(2)
	if snake2.xcor()>290 or snake2.xcor()<-290 or snake2.ycor()>290 or snake2.ycor()<-290:
		reset_game(1)


	#snake eat apple and grow
	if snake1.distance(apple)<20:
		x= random.randint(-290,290)
		y= random.randint(-290,290)
		apple.goto(x,y)
		newPart=turtle.Turtle()
		newPart.speed(0)
		newPart.shape('square')
		newPart.penup()
		newPart.color('white')
		parts.append(newPart)
	for i in range(len(parts)-1,0,-1):
		x=parts[i-1].xcor()
		y=parts[i-1].ycor()
		parts[i].goto(x,y)
	if len(parts)>0:
		x=snake1.xcor()
		y=snake1.ycor()
		parts[0].goto(x,y)

	move()
	#when snake hits own tail, snake'll die
	for i in parts:
		if i.distance(snake1)<20:
			reset_game(2)
	for i in parts:
		if i.distance(snake2)<20:
			reset_game(1)

	if snake2.distance(apple) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		apple.goto(x, y)
		newPart2 = turtle.Turtle()
		newPart2.speed(0)
		newPart2.shape('square')
		newPart2.penup()
		newPart2.color('yellow')
		parts2.append(newPart2)
	for i in range(len(parts2)-1,0,-1):
		x=parts2[i-1].xcor()
		y=parts2[i-1].ycor()
		parts2[i].goto(x,y)
	if len(parts2)>0:
		x=snake2.xcor()
		y=snake2.ycor()
		parts2[0].goto(x,y)

	move2()
	for i in parts2:
		if i.distance(snake2)<20:
			reset_game(1)
	for i in parts2:
		if i.distance(snake1)<20:
			reset_game(2)


	#screen time
	time.sleep(0.1)


