#******************************************************************************
# Author:           Michael Hendricks
# Lab:              Practice 5
# Date:             April 29, 2025
# Description:      Calculates average and high score for as many players as the user would like to enter
# Input:            playerName as string, numberOfGames as integer,
# Output:           averagePoints as int, highScore as int,
# Sources:          Practice 5 specifications and example
#******************************************************************************

# Sample Run:

#Welcome to the basketball average points calculator

#Enter your player's name: mike
#How many games did mike play: 2
#How many points did mike score in game 1: 45
#How many points did mike score in game 2: 17

#Average points for mike is 31.0
#The high score for mike was 45
#Do you want to enter another player (y/n): n

#Thank you for using the average points calculator!

def main():
    playerName = ""
    numberOfGames = 0
    totalPoints = 0
    highScore = 0
    averagePoints = 0.0
    continueGame = 'y'
    minimumPoints = None
    totalPoints = 0

    printWelcome()

    while continueGame == 'y':
        playerName = getPlayerName()
        numberOfGames = int(getNumberOfGames(playerName))

        for i in range(numberOfGames):
            pointsScored = getPoints(playerName, i + 1)
            totalPoints += pointsScored
            if pointsScored > highScore:
                highScore = pointsScored

            if minimumPoints is None or pointsScored < minimumPoints:
                minimumPoints = pointsScored

        averagePoints = calculateAveragePoints(totalPoints, numberOfGames)

        printAverage(playerName, averagePoints)
        printHighScore(playerName, highScore)
        printMinimumScore(playerName, minimumPoints)
        printTotalPoints(playerName, totalPoints)
        continueGame = input("Do you want to enter another player (y/n): ").lower()

    printGoodbye()

def printTotalPoints(playerName, totalPoints):
    """
    Prints total points of player
    :param playerName: string
    :param totalPoints: integer
    :return: None
    """
    print("Total points of " + playerName + " is " + str(totalPoints))

def printMinimumScore(playerName, minimumPoints):
    """
    Prints minimum points score
    :param playerName: string
    :param minimumPoints: integer
    :return: None
    """
    print("The minimum points score for " + playerName + "is: " + str(minimumPoints))

def getNumberOfGames(playerName: str):
    """
    Prompts and returns the number of games played as integer
    :param playerName: string
    :return: games as integer
    """
    games = input("How many games did " + playerName + " play: ")
    return games

def getPlayerName():
    """
    Prompts and returns the player's name as a string
    :return: playerName as string
    """
    name = input("Enter your player's name: ")
    return name

def printWelcome():
    """
    Prints welcome message to user
    :return: None
    """
    print("Welcome to the basketball average points calculator")

def printGoodbye():
    """
    Prints goodbye message to user
    :return: None
    """
    print("Thank you for using the average points calculator")

def getPoints(playerName: str, game: int):
    """
    Prompts and returns amount of points
    :param playerName: string
    :param game: integer
    :return: points as string
    """
    points = int(input("How many points did " + playerName + " score in game " + str(game) + ": "))
    return points

def printAverage(playerName: str, averagePoints: float):
    """
    Prints average points
    :param playerName: string
    :param averagePoints: float
    :return: None
    """
    print("Average points for " + playerName + " is " + str(round(averagePoints, 2)))

def printHighScore(playerName: str, highScore: int):
    """
    Prints high score
    :param playerName: string
    :param highScore: integer
    :return: None
    """
    print("The high score for " + playerName + " is " + str(highScore))

def calculateAveragePoints(totalPoints: int, numberOfGames: int):
    """
    Calculates average points
    :param totalPoints: integer
    :param numberOfGames: integer
    :return: average as float
    """
    avg = totalPoints / numberOfGames
    return avg

main()