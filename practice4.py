#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Practice 4
# Date:             April 27, 2025
# Description:      Prompts a user for their total change as an integer and output the
#                   change using the fewest coins, one coin type per line.
# Input:            totalChange as integer
# Output:           number of dollars as int, number of quarters as int, number if dunes as int,
#                   number of nickels as int, number of pennies as int
# Sources:          Practice 4 specifications and example
#******************************************************************************

# Sample Run:

# Welcome to the change calculator
# Input total change: 156

# 1 Dollar
# 2 Quarters
# 1 Nickel
# 1 Penny
# Goodbye!

def main():
    total_change = 0
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    print_welcome()
    total_change = get_total_change()
    dollars = total_change // 100
    total_change = total_change % 100
    quarters = total_change // 25
    total_change = total_change % 25
    dimes = total_change // 10
    total_change = total_change % 10
    nickels = total_change // 5
    total_change = total_change % 5
    pennies = total_change // 1

    if dollars > 0:
        print_dollars(dollars)
    if quarters > 0:
        print_quarters(quarters)
    if dimes > 0:
        print_dimes(dimes)
    if nickels > 0:
        print_nickels(nickels)
    if pennies > 0:
        print_pennies(pennies)

    print_goodbye()


def print_welcome():
    """
    Prints welcome message to user
    :return: None
    """
    print("Welcome to the change calculator!")

def get_total_change():
    change = int(input("Input total change: "))
    return change

def print_dollars(dollars: int):
    if dollars == 1:
        final_word = "Dollar"
    else:
        final_word = "Dollars"
    print(dollars, final_word)

def print_quarters(quarters: int):
    if quarters == 1:
        final_word = "Quarter"
    else:
        final_word = "Quarters"
    print(quarters, final_word)

def print_dimes(dimes: int):
    if dimes == 1:
        final_word = "Dime"
    else:
        final_word = "Dimes"
    print(dimes, final_word)

def print_nickels(nickels: int):
    if nickels == 1:
        final_word = "Nickel"
    else:
        final_word = "Nickels"
    print(nickels, final_word)

def print_pennies(pennies: int):
    if pennies == 1:
        final_word = "Penny"
    else:
        final_word = "Pennies"
    print(pennies, final_word)

def print_goodbye():
    """
    Prints goodbye message to user
    :return: None
    """
    print("\nGoodbye!")

main()