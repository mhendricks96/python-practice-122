#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Lab 4
# Date:             April 27, 2025
# Description:      Returns how much your cat costs to feed per year
# Input:            monthlyCansUsed as an int, monthlyCanCost as a float
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

    printWelcome()

    # Inputs
    monthlyCansUsed = getMonthlyCansUsed()
    singleCanCost = getSingleCanCost()

    # Calculations
    monthlyCanCost = calculateMonthlyCost(monthlyCansUsed, singleCanCost)
    yearlyCost = calculateYearlyCost(monthlyCanCost)

    # Output
    printResults(yearlyCost)
    print_diet_advice(monthlyCansUsed)

def getSingleCanCost():
    """
    Prompts user to enter cost of a single can of cat food
    :return: cost as float
    """
    cost = float(input("Cost for a can of cat food: "))
    return cost

def getMonthlyCansUsed():
    """
    Prompts user to enter number of monthly cans used
    :return: cans as int
    """
    cansUsed = int(input("Cans of cat food used per month: "))
    return cansUsed

def printWelcome():
    """
    Prints welcome message to user
    :return: None
    """
    print("Welcome to the cat food calculator\n")

def calculateMonthlyCost(monthlyCansUsed: int, singleCanCost: float):
    """
    Calculates monthly cost of cat food
    :param monthlyCansUsed: int
    :param singleCanCost: float
    :return: totalCost as float
    """
    monthlyCost = monthlyCansUsed * singleCanCost
    return monthlyCost


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

def printResults(yearlyCost: float):
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


    print("\nYou spend $" + format(yearlyCost, ".2f") + " on cat food per year. " + description)

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