#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Practice 2
# Date:             April 8, 2025
# Description:      use miles per gallon and price per gallon to get total gas cost
# Input:            milesPerGallon as integer, pricePerGallon as float
# Output:           cost for 20 miles, cost for 75 miles, cost for 500 miles
# Sources:          Practice 2 specifications
#******************************************************************************

# Sample Run:

# Enter the miles per gallon: 10
# Enter the price per gallon: 6.00


# Cost for 20 miles:  1200.00
# Cost for 75 miles:  4500.00
# Cost for 500 miles:  30000.00

TWENTY_MILES = 20
SEVENTY_FIVE_MILES = 75
FIVE_HUNDRED_MILES = 500

milesPerGallon = float(input("Enter the miles per gallon: "))
pricePerGallon = float(input("Enter the price per gallon: "))

costPerMile = milesPerGallon * pricePerGallon


costFor20Miles = costPerMile * TWENTY_MILES
costFor75Miles = costPerMile * SEVENTY_FIVE_MILES
costFor500Miles = costPerMile * FIVE_HUNDRED_MILES

print("Cost for 20 miles: ", format(costFor20Miles, ".2f"))
print("Cost for 75 miles: ", format(costFor75Miles, ".2f"))
print("Cost for 500 miles: ", format(costFor500Miles, ".2f"))


