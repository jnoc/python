from graphics import *
import os

#1
def personalGreeting():
    name = str(input("What is your name? "))
    greeting = name + ", nice to see you!"
    print(greeting)
#2    
def formalName():
    fore = str(input("What is your forename? "))
    sur = str(input("What is your surname? "))
    foreShort = fore[0]
    fullname = foreShort + "." + sur
    print(fullname)
#3 
def kilos2pounds():
    kilo = float(input("int: "))
    pound = kilo * 2.2046
    print(round(kilo,2), "kilos is equal to", round(pound,2),"pounds")
#4
def generateEmail():
    name = str(input("What is your name? "))
    sur = str(input("What is your surname? "))
    enroll = str(input("What year did you enroll? "))
    nameS = name[:4]
    surS = sur[0]
    enrollS = enroll[2:4]
    email = nameS + "." + surS + "." + enrollS + "@myport.ac.uk"
    print(email)
#5
def gradeTest():
    n = int(input("What mark did you get?: "))
    grade = "FFFFCCBBAAA"
    for i in [n]:
        ans = grade[i]
    print("Your mark is equal to", ans)
#6
def graphicLetters():
    word = str(input("What would you like to say? "))
    win = GraphWin("Click-able sentence", 500, 500)
    message = Text(Point(250, 30), "Click in the window to draw a letter at a time")
    message.draw(win)
    for i in range(len(word)):
        character = word[0 + i]
        p = win.getMouse()
        letter = Text(Point(p.getX(),p.getY()), character)
        letter.setSize(30)
        letter.draw(win)
#7
def singASong():
    word = str(input("What word would you like your song to be? "))
    lines = int(input("How many lines long do you want the song to be? "))
    repeat = int(input("How many times should the word be repeated? "))
    for i in range(lines):
        print("\t")
        for i in range(repeat):
            print(word, end=" ")
#8
def exchangeTable():
    for i in [0,1,2,3,4,5,6,7,8,9,10]:
        pounds = i / 1.09
        print("€", i, "\t£ ", round(pounds,2))
        
    for i in [11,12,13,14,15,16,17,18,19,20]:
        pounds = i / 1.09
        print("€", i, "\t£", round(pounds,2))
#9
def makeAcronym():
    sentence = str(input("What is your string? "))
    for i in sentence.split():
        print(i[0], end="")
#10
def nameToNumber():
    name = str(input("What is your name? "))
    nameL = name.lower()
    answer = 0
    for i in range(len(nameL)):
        letter = nameL[i]
        for i in letter:
            binaryVal = ord(i)
            part1 = binaryVal - 96
            answer = answer + part1
    print(answer)
#11
def fileInCaps():
    print("Given '..' lists the previous directory and '.' lists the current directory.")
    print("You are in", os.getcwd())
    file = str(input("What file do you want to view the contents of? "))
    print(os.listdir(file))
