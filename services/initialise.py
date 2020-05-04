from services.helpers import clearScreen
from services.ready import playerReady
from entities.game import Game

def initialiseShips(player):
    for ship in player.ships:
        print("Current Player: "+player.name)
        print("Insert Ship: {} \nLength: {} \nCurrent Board:".format(ship.shipName, ship.size))
        player.board.drawBoardShip()
        while not ship.changeOrientation(input("Please enter ship orientation (v/h):")):
            pass
        while not player.board.insertShip(ship,input("Enter the position: ")):
            pass
        clearScreen()

    print("Final Board:")
    player.board.drawBoardShip()
    input("Press enter to continue:")
    clearScreen()

def initPlayer(game):
    playerReady(game)
    initialiseShips(game.curr)
    game.changeCurrentPlayer()

def initGame():
    clearScreen()
    player1 = input("Enter Player 1 Name: ")
    while True:
        player2 = input("Enter Player 2 Name: ")
        if player1 == player2:
            print("Error: Player names cannot be the same")
        else:
            break
    game = Game(player1,player2)
    clearScreen()
    initPlayer(game)
    initPlayer(game)
    return game