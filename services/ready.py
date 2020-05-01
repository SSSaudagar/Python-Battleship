from services.helpers import clearScreen
from services.player_turn import playerTurn

def playerReady(game):
    print("\nCurrent Player: {}".format(game.curr.name))
    print("Your Health: {}".format(game.curr.getPlayerHealth()))
    input("Hide the screen from {}. \nPress \"Ctrl + C\" to exit or \"Enter\" to continue . . . ".format(game.curr.opponent.name))
    clearScreen()
    
def playGame(game):
    while not game.winner():
        playerReady(game)
        playerTurn(game)

    if game.winner():    
        print("Game Completed. {} is the winner".format(game.winner()))
    else:
        print("Game not Complete")
    input("Press Enter to exit . . .")

