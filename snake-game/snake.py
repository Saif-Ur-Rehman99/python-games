import turtle
import time
import random

delay = 0.1

# Game Window
window = turtle.Screen()
window.title('Snake Game by @saiph.py')
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer(0)

# Snake
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'stop'


# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

segments = []

# Functions
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


def go_up():
    if head.direction != 'down':
        head.direction = "up"

def go_down():
    if head.direction != 'up':
        head.direction = "down"

def go_right():
    if head.direction != 'left':
        head.direction = "right"

def go_left():
    if head.direction != 'right':
        head.direction = "left"


# Keyboard
window.listen()
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_right, 'd')
window.onkeypress(go_left, 'a')

# Main game loop
while True:
    window.update()
    
    # check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    # check for a collision with the food
    if head.distance(food) < 20:

        # Move the food to the random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)


        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)
    

    # Move the end segment first in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear th esegment list
            segments.clear()
    
    time.sleep(delay)


window.mainloop()