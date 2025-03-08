import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor('black')
screen.setup(600, 600)

# Score tracking (now directly represents apples eaten)
score1, score2 = 0, 0

def update_score():
    score_display.clear()
    score_display.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 16, "normal"))

# Snake creation
def create_snake(color, start_x):
    snake = turtle.Turtle()
    snake.shape('square')
    snake.color(color)
    snake.speed(0)
    snake.penup()
    snake.goto(start_x, 0)
    snake.direction = 'stop'
    return snake

snake1 = create_snake('white', -200)
snake2 = create_snake('yellow', 200)

# Apple setup
apple = turtle.Turtle()
apple.shape('circle')
apple.color('red')
apple.speed(0)
apple.penup()
apple.goto(0, 100)  # Start apple away from snakes

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('lightgreen')
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
update_score()

# Movement functions
def go_up1():
    if snake1.direction != 'down':
        snake1.direction = 'up'

def go_down1():
    if snake1.direction != 'up':
        snake1.direction = 'down'

def go_right1():
    if snake1.direction != 'left':
        snake1.direction = 'right'

def go_left1():
    if snake1.direction != 'right':
        snake1.direction = 'left'

def go_up2():
    if snake2.direction != 'down':
        snake2.direction = 'up'

def go_down2():
    if snake2.direction != 'up':
        snake2.direction = 'down'

def go_right2():
    if snake2.direction != 'left':
        snake2.direction = 'right'

def go_left2():
    if snake2.direction != 'right':
        snake2.direction = 'left'

def move(snake):
    if snake.direction == 'up':
        snake.sety(snake.ycor() + 20)
    elif snake.direction == 'down':
        snake.sety(snake.ycor() - 20)
    elif snake.direction == 'right':
        snake.setx(snake.xcor() + 20)
    elif snake.direction == 'left':
        snake.setx(snake.xcor() - 20)
    
    # Wrap-around feature
    if snake.xcor() > 290:
        snake.setx(-290)
    elif snake.xcor() < -290:
        snake.setx(290)
    if snake.ycor() > 290:
        snake.sety(-290)
    elif snake.ycor() < -290:
        snake.sety(290)

# Key bindings - Using direct function references instead of lambda
screen.listen()
screen.onkeypress(go_up1, 'w')    # Changed to direct function reference
screen.onkeypress(go_down1, 's')  # Changed to direct function reference
screen.onkeypress(go_right1, 'd') # Changed to direct function reference
screen.onkeypress(go_left1, 'a')  # Changed to direct function reference
screen.onkeypress(go_up2, 'Up')
screen.onkeypress(go_down2, 'Down')
screen.onkeypress(go_right2, 'Right')
screen.onkeypress(go_left2, 'Left')

# Snake body lists
parts1, parts2 = [], []

def reset_snake(snake, parts, start_x):
    # Reset snake position
    snake.goto(start_x, 0)
    snake.direction = 'stop'
    
    # Clear body parts
    for part in parts:
        part.goto(2000, 2000)  # Move off-screen
        part.hideturtle()  # Hide the turtle
    parts.clear()

def check_tail_collision(snake, parts):
    # Check if snake collides with its own tail
    for part in parts:
        if part.distance(snake) < 20:
            return True
    return False

def check_head_collision(snake1, snake2):
    # Check if snake heads collide
    if snake1.distance(snake2) < 20:
        return True
    return False

def grow_snake(snake, parts, color, amount=1):
    for _ in range(amount):
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape('square')
        new_part.penup()
        new_part.color(color)
        new_part.hideturtle()  # Initially hidden until positioned
        parts.append(new_part)

def update_body(parts, snake):
    for i in range(len(parts) - 1, 0, -1):
        x, y = parts[i - 1].xcor(), parts[i - 1].ycor()
        parts[i].goto(x, y)
        parts[i].showturtle()  # Make sure it's visible after positioning
    
    if parts:
        parts[0].goto(snake.xcor(), snake.ycor())
        parts[0].showturtle()

# Main game loop
while True:
    screen.update()
    
    # Move and update body first
    update_body(parts1, snake1)
    update_body(parts2, snake2)
    
    # Then move the heads
    move(snake1)
    move(snake2)
    
    # Check if snakes eat apple
    if snake1.distance(apple) < 20:
        apple.goto(random.randint(-280, 280), random.randint(-280, 280))
        grow_snake(snake1, parts1, 'white')
        score1 += 1  # Increase score directly when eating an apple
        update_score()
    
    if snake2.distance(apple) < 20:
        apple.goto(random.randint(-280, 280), random.randint(-280, 280))
        grow_snake(snake2, parts2, 'yellow')
        score2 += 1  # Increase score directly when eating an apple
        update_score()
    
    # Check for tail collisions
    if check_tail_collision(snake1, parts1[1:]):  # Skip head position
        reset_snake(snake1, parts1, -200)
        score1 = 0  # Reset score when dying
        update_score()
    
    if check_tail_collision(snake2, parts2[1:]):  # Skip head position
        reset_snake(snake2, parts2, 200)
        score2 = 0  # Reset score when dying
        update_score()
    
    # Check for collisions with opponent's tail
    for part in parts2:
        if part.distance(snake1) < 20:
            reset_snake(snake1, parts1, -200)
            score1 = 0  # Reset score when dying
            update_score()
            break
    
    for part in parts1:
        if part.distance(snake2) < 20:
            reset_snake(snake2, parts2, 200)
            score2 = 0  # Reset score when dying
            update_score()
            break
    
    # Check for head-to-head collision
    if check_head_collision(snake1, snake2):
        # Determine which snake is bigger based on score/length
        if score1 > score2:
            # Snake 1 eats Snake 2
            reset_snake(snake2, parts2, 200)
            
            # Transfer points (grow snake1 by snake2's score)
            grow_snake(snake1, parts1, 'white', score2)
            score1 += score2  # Add opponent's score
            score2 = 0        # Reset opponent's score
            update_score()
                
        elif score2 > score1:
            # Snake 2 eats Snake 1
            reset_snake(snake1, parts1, -200)
            
            # Transfer points (grow snake2 by snake1's score)
            grow_snake(snake2, parts2, 'yellow', score1)
            score2 += score1  # Add opponent's score
            score1 = 0        # Reset opponent's score
            update_score()
                
        # If scores are equal, nothing happens - they pass through each other
    
    time.sleep(0.1)
