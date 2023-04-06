import turtle
import random

## 함수 선언 부분 ##
def  screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    
    tSize = random.randrange(1, 10)
    angle = random.randrange(1, 361)
    turtle.shapesize(tSize)
    
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    turtle.right(angle)
    turtle.color(r,g,b)
    turtle.stamp()

def  screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def  screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
angle = 0
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
