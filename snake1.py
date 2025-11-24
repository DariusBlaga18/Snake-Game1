import turtle
import time
import random

score = 0
high_score = 0
segments = []

screen = turtle.Screen()
screen.title("Snake Game 1")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.speed(0)

head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)
food.shapesize(0.8)
food.speed(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}\nHigh Score: {high_score}", font = ("Courier", 24, "bold"))

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

def move():
    if head.direction == "up":
        head.sety( head.ycor() + 20)
    if head.direction == "down":
        head.sety( head.ycor() - 20)
    if head.direction == "right":
        head.setx( head.xcor() + 20)
    if head.direction == "left":
        head.setx( head.xcor() - 20)

while True:
    
    screen.update()
    time.sleep(0.1)
    
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto( segments[i-1].xcor(), segments[i-1].ycor() )
    if len(segments) > 0:
        segments[0].goto( head.xcor(), head.ycor() )
    
    move()
   
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear() 
    
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for s in segments:
                s.goto(1000, 1000)

            segments.clear()
 
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}\nHigh Score: {high_score}", align="center", font=("Courier", 24, "bold"))
            
          





