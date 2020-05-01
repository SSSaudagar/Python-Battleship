from services.helpers import clearScreen

def playerReady(game):
    print("Current Player: {}".format(game.curr.name))
    print("Player Health: {}".format(game.curr.getPlayerHealth()))
    input("Hide the screen from {}. Press enter to continue . . . ".format(game.curr.opponent.name))
    clearScreen()