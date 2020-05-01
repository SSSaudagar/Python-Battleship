from services.helpers import clearScreen

def initialiseShips(player):
    for ship in player.ships:
        print("Current Player: "+player.name)
        print("Insert Ship: {} \nLength: {} \nCurrent Board:".format(ship.shipName, ship.size))
        player.board.drawBoardShip()
        ship.changeOrientation(input("Please enter ship orientation (vertical/horizontal):"))
        while not player.board.insertShip(ship,int(input("Enter the position: "))):
            print("Incorrent Input.")
        clearScreen()

    print("Final Board:")
    player.board.drawBoardShip()
    input("Press enter to continue:")
    clearScreen()