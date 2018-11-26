#-------------------------------------------------------------------------------
# Practical Worksheet 8: Design and Simulation
# coinflips.py
#-------------------------------------------------------------------------------
from random import random

def getInputs():
    # asks the user for their input of coin flips
    amount = int(input("How many times would you like the coin to flip? " ))
    simulateFlips(amount)

def simulateFlips(amount):
    # main bulk of program
    heads = 0
    tails = 0
    for i in range(amount):
        number = random() 
        if number < 0.5:
            heads = heads + 1 / amount
        else:
            tails = tails + 1 / amount
    displayResults(heads, tails)

def displayResults(heads, tails):
    # this shows the proportion of the heads to tails ie how many heads to tails that were flipped
    print("Heads", round(heads, 3), ":", "Tails", round(tails, 3))
    input("\nPress enter to close...")

def main():
    # executes the program
    getInputs()
main()