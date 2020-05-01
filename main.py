from entities.game import Game
from services.initialise import initialiseShips
from services.helpers import clearScreen

clearScreen()




player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")
game = Game(player1,player2)

def playerReady():
    print("Current Player: {}".format(game.curr.name))
    print("Player Health: {}".format(game.curr.getPlayerHealth()))
    input("Hide the screen from {}. Press enter to continue . . . ".format(game.curr.opponent.name))
    clearScreen()

clearScreen()
playerReady()
initialiseShips(game.p1)
game.changeCurrentPlayer()

playerReady()
initialiseShips(game.p2)
game.changeCurrentPlayer()



while not game.winner():
    playerReady()
    print("Current Player: {}".format(game.curr.name))
    print("Player Health: {}".format(game.curr.getPlayerHealth()))
    print("Your Ship Board:")
    game.curr.board.drawBoardShip()
    print("Attack Board:")
    game.curr.opponent.board.drawBoardAttack()
    attack = int(input("Enter the position to attack:"))
    clearScreen()
    game.curr.opponent.board.attack(attack)
    game.changeCurrentPlayer()
    

print("{} is the winner".format(game.winner))
