    #---------------------------------------------------
    # Practical Worksheet 3: Graphical Programming
    # October 2018
    #---------------------------------------------------

from graphics import *

#1
def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    body = Line(Point(100, 80), Point(100, 120))
    leftL = Line(Point(100, 120), Point(80, 170))
    rightL = Line(Point(100, 120), Point(120, 170))
    leftA = Line(Point(100, 80), Point(80, 120))
    rightA = Line(Point(100, 80), Point(120, 120))
    head.draw(win),body.draw(win),leftL.draw(win),rightL.draw(win),leftA.draw(win),rightA.draw(win)
#2
def drawCircle():
    win = GraphWin("Radius Circle")
    radius = float(input("What is the raidus of the circle? (Pixels) "))
    center = Point(100, 100)
    c = Circle(center, radius)
    c.draw(win)
#3
def drawArcheryTarget():
    win = GraphWin("Archery")
    center = Point(100, 100)
    radius = 30
    yellow = Circle(center, radius)
    red = Circle(center, radius * 2)
    blue = Circle(center, radius * 3)
    blue.draw(win),red.draw(win),yellow.draw(win)
    yellow.setFill("yellow"),red.setFill("red"),blue.setFill("blue")
#4
def drawRectangle():
    print("Inputs have to be below 200 to see it.")
    height = float(input("What is the height of your rectangle? "))
    width = float(input("What is the width of your rectangle? "))
    x = height / 2
    y = width / 2
    win = GraphWin("Centered rectangle")
    x1, y1 = 100 - x, 100 - y
    x2, y2 = 100 + x, 100 + y
    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    rectangle.draw(win)
    center = Point(100, 100)
    center.draw(win)
#5
def blueCircle():
    win = GraphWin("Blue Circle", 500, 500)
    message = Text(Point(250, 50),"Click in the window to draw a circle with a 50 pixel radius")
    message.draw(win)
    p = win.getMouse()
    point = Point(p.getX(), p.getY())
    c = Circle(point, 50)
    message.setText("")
    c.draw(win)
    c.setFill("blue")

#6 would be cool to get the coords and work out the gradient of the drawn line ;)
def drawLine():
    win = GraphWin("Line drawer", 500, 500)
    for i in range(10):
        message = Text(Point(250,50), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")
#7
def tenStrings():
    win = GraphWin("10 Strings", 500, 500)
    message = Text(Point(250, 30), "Enter your 'string'")
    message.draw(win)
    for i in range(10):
        inputBox = Entry(Point(250, 50), 20)
        inputBox.draw(win)
        p = win.getMouse()
        string = Text(Point(p.getX(),p.getY()), inputBox.getText())
        string.draw(win)
#8
def tenColouredRectangles():
    win = GraphWin("10 Coloured rectangles", 500, 500)
    message = Text(Point(250, 30), "Pick your colour")
    message.draw(win)
    for i in range(10):
        inputBox = Entry(Point(250, 50), 5)
        inputBox.setText("blue")
        inputBox.draw(win)
        p = win.getMouse()
        x1, y1 = p.getX(),p.getY()
        p = win.getMouse()
        x2, y2 = p.getX(),p.getY()
        rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
        rectangle.draw(win)
        rectangle.setFill(inputBox.getText())
        print(i + 1)
#10
def plotRainfall():
    win = GraphWin("Plot the weeks rainfall", 400, 400)
    xaxis = Line(Point(70, 300), Point(300, 300))
    xaxis.draw(win)
    yaxis = Line(Point(70, 300), Point(70, 30))
    yaxis.draw(win)
    for i in [0, 30, 60, 90, 120, 150, 180, 210, 240, 270]:
        ymessage = Text(Point(50, 300 - i), i)
        ymessage.draw(win)
    p = 0
    for i in [80,110,140,170,200,230,260]:
        amount = int(input("How much rain fell? (mm) "))
        rectangle = Rectangle(Point(i, 300 - amount),Point(i + 30, 300))
        rectangle.draw(win)
        p = p + 1
        xmessage = Text(Point(i + 15, 310), p)
        xmessage.draw(win)
