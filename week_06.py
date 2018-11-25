    #---------------------------------------------------
    # Practical Worksheet 6: if statements and for loops
    # November 2018
    #---------------------------------------------------

from graphics import *
import math

#1
def fastFoodOrderPrice():
    order = float(input("What is the price of your order? £"))
    if order >= 10:
        print("Your order costs £" + str(order))
    elif order < 10:
        print("Your order costs £" + str(order + 1.50))
#2
def whatToDoToday():
    temp = int(input("What is the temprature today? "))
    if temp >= 25:
        print("Go for a swim in the sea?")
    elif temp >= 10:
        print("Go shopping at Gunwharf Quays?")
    else:
        print("Movie time at home?")
#3
def displaySquareRoots(start, end):
    for i in range(start, end + 1):
        ans = math.sqrt(i)
        print("The square root of", i, "is", round(ans,3))
#4
def calculateGrade(grade):
    if grade > 20 or grade < 0:
        print("X")
    elif grade >= 16:
        print("Your grade is a A")
    elif grade >= 12:
        print("Your grade is a B")
    elif grade >= 8:
        print("Your grade is a C")
    else:
        print("Your grade is a F")
#5
def peasInAPod(peas):
    win = GraphWin("'Peas in a pod'",100 * peas, 100)
    move = 0
    for i in range(peas):
        c = Circle(Point(50 + move, 50), 50)
        c.draw(win)
        c.setFill("green")
        move = move + 100
#6
def ticketPrice(distance, age):
    ticket = 3 + (0.15 * distance)
    discount = ticket - (ticket * 0.4)
    if age >= 60:
        print("Your ticket price is £" + str(discount))
    elif age <= 15:
        print("Your ticket price is £" + str(discount))
    else:
        print("Your ticket price is £" + str(ticket))
#7
def numberedSquare(n):
    for i in range(n,0,-1):
        for j in range(n):
            print(i+j, end=" ")
        print()
#8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
#8
def drawColouredEye(win, centre, r, colour):
    for radius in [r, r/2, r/4]:
        if radius == r:
            drawCircle(win, centre, radius, "white")
        elif radius == r/2:
            drawCircle(win, centre, radius, colour)
        else:
            drawCircle(win, centre, radius, "black")

def eyePicker():
    print("a = blue, b = grey, c = green and d = brown")
    colour = str(input("What colour do you want the eye to be? "))
    radius = float(input("What do you want the eye radius to be? "))
    x = float(input("What is your x center point? "))
    y = float(input("What is your y center point? "))
    
    centre = Point(x,y)
    if x and y > radius:
        win = GraphWin("Eye Picker", x * 2, y * 2)
        if colour == "a":
            drawColouredEye(win, centre, radius, "blue")
        elif colour == "b":
            drawColouredEye(win, centre, radius, "grey")
        elif colour == "c":
            drawColouredEye(win, centre, radius, "green")
        elif colour == "d":
            drawColouredEye(win, centre, radius, "brown")
        else:
            print("That colour is invalid!")
    else:
        print("The eye will be too big for the graphical window")
#9
def drawPatchWindow1():
    win = GraphWin("Patch", 200, 200)
    line = Line(Point(50, 50), Point(150, 150))
    line.draw(win)
    for i in range(0, 101, 10):
        add = 50 + i
        minus = 150 - i
        lines = Line(Point(add, 50), Point(minus, 150))
        lines.draw(win)
        lines.setOutline("red")
        lines = Line(Point(50, add), Point(150, minus))
        lines.draw(win)
        lines.setOutline("red")
    rectangle = Rectangle(Point(50, 50), Point(150, 150))
    rectangle.draw(win)
    
def drawPatchWindow2():
    win = GraphWin("Patch", 200, 200)    
    for i in [0, 20, 40, 60, 80]:
        for j in [20, 40, 60, 80, 100]:
            rectangle = Rectangle(Point(i, i), Point(j, j))
            rectangle.setOutline("red")
            rectangle.draw(win)
    for i in [10, 30, 50, 70, 90]:
        for j in [10, 30, 50, 70, 90]:
            hi = Text(Point(i, j), "hi!")
            hi.setOutline("red")
            hi.setSize(5)
            hi.draw(win)
#10
def drawPatch(win, x, y, colour):   
    for i in [0, 20, 40, 60, 80]:
        for j in [20, 40, 60, 80, 100]:
            rectangle = Rectangle(Point(x + i, y + i), Point(x + j, y + j))
            rectangle.setOutline(colour)
            rectangle.draw(win)
    for i in [10, 30, 50, 70, 90]:
        for j in [10, 30, 50, 70, 90]:
            hi = Text(Point(x + i, y + j), "hi!")
            hi.setOutline(colour)
            hi.setSize(5)
            hi.draw(win)

def drawPatchWork():
    win = GraphWin("Patches", 301, 201)
    for x in [0, 100, 200]:
        for y in [0, 100]:
            drawPatch(win, x, y, "blue")

#11
def eyesAllAround():
    win = GraphWin("Patch", 800, 600)
    a = "blue"
    b = "grey"
    c = "green"
    d = "brown"
    for i in range(8):
        if i <= 6:
            for j in [a,b,c,d]:
                p = win.getMouse()
                centre = Point(p.getX(), p.getY())
                radius = 30
                drawColouredEye(win, centre, radius, j)
        elif i == 7:
            for j in [a,b]:
                p = win.getMouse()
                centre = Point(p.getX(), p.getY())
                radius = 30
                drawColouredEye(win, centre, radius, j)
