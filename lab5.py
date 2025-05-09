#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Lab 5
# Date:             May 4, 2025
# Description:      Returns how much your cats costs to feed per year
# Input:            monthlyCansUsed as an int, monthlyCanCost as a float, catName as a string
# Output:           yearlyCost as a float, healthAdvice as a string
# Sources:          Lab 4 specifications and example
#******************************************************************************

# Welcome to the cat food calculator and diet checker

# Cans of cat food used per month: 10
# Cost for a can of cat food: 2.00

# You spend $240 on cat food per year. That's chump change!
# TThat's a good amount of cat food to feed your cat!

def main():

    # Initialize variables
    monthlyCansUsed = 0
    singleCanCost = 0.00
    monthlyCanCost = 0.00
    yearlyCost = 0.00
    anotherCat = 'y'
    catName = ''

    printWelcome()

    while anotherCat == 'y' or anotherCat == 'Y':

        catName = getCatName()
        # Inputs
        monthlyCansUsed = getMonthlyCansUsed(catName)
        singleCanCost = getSingleCanCost(catName)

        # Calculations
        monthlyCanCost = calculateMonthlyCost(monthlyCansUsed, singleCanCost)
        yearlyCost = calculateYearlyCost(monthlyCanCost)

        # Output
        printResults(yearlyCost, catName)
        print_diet_advice(monthlyCansUsed)

        anotherCat = askToContinue()

    printGoodbye()

def getSingleCanCost(catName: str):
    """
    Prompts user to enter cost of a single can of cat food
    :return: cost as float
    """
    cost = float(input("Cost for a can of cat food for " + catName + ": "))
    return cost

def askToContinue():
    """
    Asks user if they want to add another cat
    :return: answer as str
    """
    answer = input("Would you like to add another cat? (y/n): ")
    return answer

def getMonthlyCansUsed(catName: str):
    """
    Prompts user to enter number of monthly cans used
    :return: cans as int
    """
    cansUsed = int(input("Cans of cat food used per month for " + catName + ": "))
    return cansUsed

def printWelcome():
    """
    Prints welcome message to user
    :return: None
    """
    print("Welcome to the cat food calculator\n")

def printGoodbye():
    """
    Prints goodbye message to user
    :return: None
    """
    print("Thank you for using the cat food calculator!")

def calculateMonthlyCost(monthlyCansUsed: int, singleCanCost: float):
    """
    Calculates monthly cost of cat food
    :param monthlyCansUsed: int
    :param singleCanCost: float
    :return: totalCost as float
    """
    monthlyCost = monthlyCansUsed * singleCanCost
    return monthlyCost

def getCatName():
    """
    Prompts user to enter cat food name
    :return: catName as str
    """
    name = input("Your cats name: ")
    return name


def calculateYearlyCost(monthlyCost: float):
    """
    Calculates yearly cost of cat food
    :param monthlyCost: float
    :return: yearlyCost as float
    """
    # Constant
    MONTHS_IN_YEAR = 12

    yearlyCost = monthlyCost * MONTHS_IN_YEAR
    return yearlyCost

def printResults(yearlyCost: float, catName: str):
    """
    Prints results of calculation
    :param yearlyCost: float
    :return: None
    """
    description = ""
    if yearlyCost < 250:
        description = "That's chump change!"
    elif yearlyCost > 500:
        description = "Make sure you add that to your budget!"
    else:
        description = "not bad, not great"


    print("\nYou spend $" + format(yearlyCost, ".2f") + " on cat food per year for " + catName + ". " + description)

def print_diet_advice(monthlyCans):
    healthAdvice = ""
    if monthlyCans < 10:
        healthAdvice = "That cat is all skin and bones! Feed that thing!"
    elif monthlyCans > 20:
        healthAdvice = "Wow! what a chunker. Maybe a diet is in order"
    else:
        healthAdvice = "That's a good amount of cat food to feed your cat!"

    print(healthAdvice)


main()