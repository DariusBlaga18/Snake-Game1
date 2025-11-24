import turtle
import time

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
    move()