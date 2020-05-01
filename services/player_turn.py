from services.ready import playerReady
from services.helpers import clearScreen

def playerTurn(game):
    
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