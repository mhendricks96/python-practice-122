#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Practice 6
# Date:             May 11, 2025
# Description:      Banking program that allows user to view balance, make deposit,
#                   or withdraw funds
# Input:            choice as string, depositAmount as float, withdrawAmount as float
# Output:           balance as float
# Sources:          Practice 6 specifications and example
#******************************************************************************

import valid as v

# Welcome to PCC Credit Union

# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit

# Enter choice: 1
# Account balance: $ 0.00

# Enter choice: 2
# Enter deposit amount $ 150.60

# Enter choice: 1
# Account balance: $ 150.60

# Enter choice: 3
# Enter withdraw amount $ 10.23

# Enter choice: 1
# Account balance: $ 140.37

# Enter choice: 4

# Thank you for using PCC Credit Union!


QUIT = 4


def main():
    choice = 0
    balance = 0.0

    print("Welcome to PCC Credit Union")

    print_menu()

    while choice != QUIT:
        choice = get_choice()
        if choice == 1:
            view_balance(balance)
        elif choice == 2:
            deposit = get_deposit_amt()
            balance = balance + deposit
        elif choice == 3:
            withdraw = get_withdraw_amt(balance)
            balance = balance - withdraw

    print("\nThank you for using PCC Credit Union!")


def print_menu():
    """
    Function to print the menu to view balance, make deposit, or withdraw funds
    :return: none
    """
    print("\n1. View balance")
    print("2. Make deposit")
    print("3. Withdraw funds")
    print("4. Quit")


def view_balance(balance):
    """
    Function to print current account balance.
    :param balance: float, current account balance
    :return: none
    """
    print("Account balance: $", format(balance, ".2f"))

def get_choice():
    """
    prompts for and returns a valid option for the menu choice: integers 1, 2, 3, 4.
    :return: userChoice as integer
    """
    prompt = "\nEnter choice: "
    userChoice = v.get_integer(prompt)

    while 0 < userChoice < 5:
        return userChoice
    else:
        print("That is not a valid choice.")

def get_deposit_amt():
    """
    prompts for and returns a valid deposit amount: real numbers greater than or equal to 0
    :return: amount as float
    """
    while True:
        amount = v.get_real("Enter deposit amount $ ")
        if amount >= 0.0:
            return amount
        else:
            print("You can only deposit a non-negative amount. Try again.")


def get_withdraw_amt(balance: float):
    """
    prompts for and returns a valid withdrawal amount: real numbers greater than or equal to 0
    AND less than or equal to the current balance
    :return:
    """
    while True:
        amount = v.get_real("Enter withdraw amount $ ")
        print("Entered amount:", amount)
        if 0.0 <= amount <= balance:
            return amount
        else:
            print("This amount cannot be withdrawn. Try again.")
main()