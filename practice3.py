#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Practice 3
# Date:             April 18, 2025
# Description:      Calculates how many gumballs will fill a cylinder jar
# Input:            diameter as float, height as float
# Output:           number of gumballs as int
# Sources:          Practice 3 specifications and example
#******************************************************************************

# Sample Run:

# Gumball Estimator!
# Enter the dimensions of a cylinder jar and I will
# tell you how many gumballs it will take to fill!

# Enter cylinder diameter (inches): 7
# Enter cylinder height (inches): 10

# The jar will hold 477 gumballs!

# Goodbye!

def main():

    diameter = 0.0
    radius = 0.0
    height = 0.0
    cylinder_volume = 0.0
    num_gumballs = 0

    print_welcome()
    print_instructions()

    # Inputs
    diameter = get_diameter()
    height = get_height()

    # Calculate the radius to use in the volume formula
    radius = calculate_radius(diameter)
    cylinder_volume = calculate_cylinder_volume(radius, height)
    num_gumballs = calculate_num_gumballs(cylinder_volume)

    # Outputs
    print_results(num_gumballs)
    print_goodbye()


def print_welcome():
    """
    Prints welcome message to user
    :return: None
    """
    print("Gumball Estimator!")

def print_instructions():
    """
    Prints instructions to user
    :return: None
    """
    print("Enter the dimensions of a cylinder jar and I will")
    print("tell you how many 1\" gumballs it will take to fill!")

def get_diameter():
    """
    Prompts user to enter diameter of cylinder
    :return: diameter as float
    """
    inputted_diameter = float(input("Enter cylinder diameter (in): "))
    return inputted_diameter

def get_height():
    """
    Prompts user to enter height of cylinder
    :return: height as float
    """
    inputted_height = float(input("Enter cylinder height (in): "))
    return inputted_height

def calculate_radius(diameter: float):
    """
    Calculates radius of cylinder
    :param diameter: float
    :return: radius as float
    """
    radius = diameter / 2.0
    return radius

def calculate_cylinder_volume(radius, height):
    """
    Calculates the volume of a cylinder
    :param radius: float
    :param height: float
    :return: volume as float
    """
    PERCENT_SOLID = .65  # percentage of cylinder that will contain solids
    # to account for space between gumballs
    PI = 3.14159265
    # Calculate the volume of cylinder = πr^2h
    # Multiply cylinder volume by 64% to account for empty space
    # between gumballs
    volume = (PI * radius ** 2 * height) * PERCENT_SOLID
    return volume

def calculate_num_gumballs(cylinder_volume: float):
    """
    Calculates the number of gumballs needed for a cylinder
    :param cylinder_volume: float
    :return: number of gumballs as int
    """
    GUMBALL_VOLUME = 0.5236  # gumball with 1" diameter
    # Calculate the number of gumballs and then truncate the decimal
    # portion - we want the whole number of gumballs
    number_of_gumballs = int(cylinder_volume / GUMBALL_VOLUME)
    return number_of_gumballs

def print_results(num_gumballs: int):
    """
    Prints results of calculation
    :param num_gumballs: int
    :return: None
    """
    print("\nThe jar will hold", num_gumballs, "gumballs!")

def print_goodbye():
    """
    Prints goodbye message to user
    :return: None
    """
    print("\nGoodbye!")


main()