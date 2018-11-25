    #---------------------------------------
    # Practical Worksheet 5: Using functions
    # Octobber 2018
    #---------------------------------------

from graphics import *
import math

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * (radius ** 2)
#1
def circumferenceOfCircle(radius):
    return  (2 * math.pi) * radius 
#2
def circleInfo():
    radius = float(input("What is the radius of your circle? "))
    print("The area is", round(areaOfCircle(radius), 3), "and the circumference is", round(circumferenceOfCircle(radius), 3))


# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
#3
def drawBrownEyeInCentre():
    win = GraphWin()
    centre = Point(100, 100)
    for radius in [60, 30, 15]:
        if radius == 60:
            colour = "white"
            drawCircle(win, centre, radius, colour)
        elif radius == 30:
            colour = "brown"
            drawCircle(win, centre, radius, colour)
        else:
            colour = "black"
            drawCircle(win, centre, radius, colour)
#4
def drawBlockOfStars(width, height):
    star = "*"
    for i in range(height):
        print("\t")
        for i in range(width):
            print(star, end=" ")

def drawLetterE():
    # E
    for i in [7, 2, 4, 2, 7]:
        width = i
        height = 2
        drawBlockOfStars(width, height)

# For exercise 5
def drawBrownEye(win, centre, r):
    for radius in [r, r/2, r/4]:
        if radius == r:
            drawCircle(win, centre, radius, "white")
        elif radius == r/2:
            drawCircle(win, centre, radius, "brown")
        else:
            drawCircle(win, centre, radius, "black")
#5
def drawPairOfBrownEyes():
    win = GraphWin("Eyes", 320, 200)
    radius = 60
    for centre in (Point(100, 100), Point(220, 100)):
        drawBrownEye(win, centre, radius)
#6
def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY() 
    x2 = p2.getX()
    y2 = p2.getY()
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
#7
def drawBlocks(gap1, width1, gap2, width2, height):
    star = "*"
    space = " "
    for a in range(height):
        print("\t")
        for b in range(gap1):
            print(space, end="")
        for c in range(width1):
            print(star, end=" ")
        for d in range(gap2):
            print(space, end="")
        for e in range(width2):
            print(star, end=" ")
#7b
def drawLetterA():
    # A
    drawBlocks(1, 6, 0, 0, 2)
    drawBlocks(0, 2, 6, 2, 2)
    drawBlockOfStars(7, 2)
    for i in range(2):
        drawBlocks(0, 2, 6, 2, 2)
#8
def drawFourPairsOFBrownEyes():
    win = GraphWin("Eyes 4", 500, 500)
    for i in range(2):
        p = win.getMouse()
        a = win.getMouse()
        for centre in (Point(p.getX(), p.getY()), Point(p.getX() + distanceBetweenPoints(p, a) * 2, p.getY())):
            drawBrownEye(win, centre, distanceBetweenPoints(p, a))
