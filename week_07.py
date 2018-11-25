#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# Novemeber 2018
#-------------------------------------------------------------------------------

from graphics import *
import time
import random as ran

#1
def getString1():
    while True:
        name = str(input("What is your name? "))
        if name.isalpha():
            break
    return name
#2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        time.sleep(3)
        amber.setFill("yellow")
        time.sleep(3)
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(3)
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(3)
        red.setFill("red")
        amber.setFill("black")
        green.setFill("black")
#3
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

def gradeCoursework():
    mark = int(input("What mark did you get in your coursework? "))
    while mark > 20 or mark < 0:
        mark = int(input("Your mark was invalid, re-enter please: "))
    while mark < 20 or mark > 0:
        calculateGrade(mark)
        break
#4
def orderPrice():
    ans = 0
    while True:
        price = float(input("What is the price of the product? "))
        products = int(input("What is the volume of the product? "))
        anymore = str(input("Do you have anymore products? (y/n) "))
        ans = ans + (price * products)
        if anymore == "n":
            break
    print("Your cost is £", ans)
#5
def clickableEye():
    pass

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
#6
def tempratureConverter():
    while True:
        temp = int(input("What is the digit you would like to convert? "))
        choice = str(input("What way would you like it converted? (FtoC / CtoF) "))
        if choice == "FtoC":
            print("Your conversion is =", fahrenheit2Celsius(temp))
        elif choice == "CtoF":
            print("Your conversion is =", celsius2Fahrenheit(temp))
        else:
            print("Invalid conversion type!")
        anymore = str(input("Do you want to proceed? (y/n) "))
        if anymore == "n":
            break
#7
def guessNumber():
    number = ran.randint(1, 100)
    print(number)
    print("You have 7 guesses, good luck!")
    for i in range(7):
        guess = int(input("What is your guess? "))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high!")
        elif guess == number:
            print("You win!")
            break
        if i == 6:
            print("You lose! The answer was", number)
