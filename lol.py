import turtle
import random
import time

delay = 0.1

window = turtle.Screen()
window.title("Dee's Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

snack = turtle.Turtle()
snack.speed(0)
snack.shape("circle")
snack.color("red")
snack.penup()
snack.goto(0,100)

body = []


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def goUp():
    head.direction = "up"

def goDown():
    head.direction = "down"

def goLeft():
    head.direction = "left"

def goRight():
    head.direction = "right"

window.listen()
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "Down")
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")

while True:
    window.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for pieces in body:
            pieces.goto(1000,1000)
        body.clear()

    if head.distance(snack) < 15:
        snack.goto(random.randint(-290,290), random.randint(-290,290))

        moreBody = turtle.Turtle()
        moreBody.speed(0)
        moreBody.shape("square")
        moreBody.color("grey")
        moreBody.penup()
        body.append(moreBody)

    for index in range(len(body)-1,0,-1):
        body[index].goto(body[index-1].xcor(), body[index-1].ycor())
    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    move()

    time.sleep(delay)


window.mainloop()
