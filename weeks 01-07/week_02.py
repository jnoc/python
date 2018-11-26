    #---------------------------------------------------
    # Practical Worksheet 2: Working with Numeric Types
    # October 2018
    #---------------------------------------------------

import math

#1
def circumferenceOfCircle():
    print("Work out the cicumference of your circle.")
    radius = float(input("What is the radius of your circle? "))
    cir = 2 * math.pi * radius
    print("The circumference of your circle is", cir)
#2
def areaOfCircle():
    print("Work out the area of your circle.")
    radius = float(input("What is the radius of your circle? "))
    area = math.pi * radius ** 2
    print("The area of your circle is", area)
#3
def costOfPizza():
    print("Work out the cost of your pizza in pence in respective to its diameter.")
    diam = float(input("What is the diameter of your circle? "))
    area = math.pi * (diam / 2) ** 2
    cost = area * 1.5
    print("The cost of your pizza will be", str(round(cost)) + "p")
#4
def slopeOfLine():
    print("Work out the gradient of a line.")
    x1 = float(input("What is your x1 value? "))
    y1 = float(input("What is your y1 value? "))
    x2 = float(input("What is your x2 value? "))
    y2 = float(input("What is your y2 value? "))
    ans = (y2 - y1) / (x2 - x1)
    print("The gradient of your line is", ans)
#5
def distanceBetweenPoints():
    print("Work out the distance between 2 coordinates.")
    x1 = float(input("What is your x1 value? "))
    y1 = float(input("What is your y1 value? "))
    x2 = float(input("What is your x2 value? "))
    y2 = float(input("What is your y2 value? "))
    ans = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance of your line is", ans)
#6
def travelStatistics():
    print("Find the overall distance and amount of fuel used within your journey.")
    avspeed = float(input("What was your journeys average speed? "))
    hour = float(input("How many hour(s) was your journey? "))
    distance = avspeed * hour
    fueleff = distance / 5
    print("Your overall distance travelled was", str(distance) + "km")
    print("The fuel efficiency of your journey was only", fueleff, "litres of fuel used")
#7
def sumOfNumbers():
    print("A sum of numbers from a given number.. ie(3 would be 1 + 2 + 3 = 6)")
    n = int(input("Enter 'n': "))
    p = 0
    for i in range(n + 1):
        
       # print("i=", i)
       # print("p=", p)
       # print("------")
        p = p + i
       # print(p)
       # print("------")
    print("The sum is...", p)
#8 [HARD]
def averageOfNumbers():
    print("An average of 'n' amount of numbers.")
    n = int(input("How many numbers is it? "))
    p = 0
    for i in range(n):
        print("Number", i + 1, ": ", end="")
        x = float(input())
        p = p + x
        amount = p
    average = amount / n
    print(average)
#9 [HARD]
def selectCoins():
    n = int(input("How many pence do you have? "))
    print("-------")
    for i in [200,100,50,20,10,5,2,1]:
        if i >= 99:
            coin = "£" + str(int(i / 100)) + "\t"
        else:
            coin = str(i) + "p\t"
        ans = str(int(n // i))
        print(coin + ": " + ans)
        print("-------")
        remain = n % i
        n = remain
