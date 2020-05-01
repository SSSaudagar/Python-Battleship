from services.helpers import clearScreen
from services.ready import playerReady

def initialiseShips(player):
    for ship in player.ships:
        print("Current Player: "+player.name)
        print("Insert Ship: {} \nLength: {} \nCurrent Board:".format(ship.shipName, ship.size))
        player.board.drawBoardShip()
        ship.changeOrientation(input("Please enter ship orientation (v/h):"))
        while not player.board.insertShip(ship,int(input("Enter the position: "))):
            print("Incorrent Input.")
        clearScreen()

    print("Final Board:")
    player.board.drawBoardShip()
    input("Press enter to continue:")
    clearScreen()

def initPlayer(game):
    playerReady(game)
    initialiseShips(game.curr)
    game.changeCurrentPlayer()
