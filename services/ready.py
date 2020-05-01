from services.helpers import clearScreen

def playerReady(game):
    print("\nCurrent Player: {}".format(game.curr.name))
    print("Your Health: {}".format(game.curr.getPlayerHealth()))
    input("Hide the screen from {}. \nPress \"Ctrl + C\" to exit or \"Enter\" to continue . . . ".format(game.curr.opponent.name))
    clearScreen()
    