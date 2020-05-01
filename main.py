from os import system, name 
from entities.game import Game

player1 = 'shashank'
player2 = 'siddharth'

game = Game(player1,player2)

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


def initialiseShips(player):
    for ship in player.ships:
        print("Current Player: "+player.name)
        print("Insert Ship: {} \nLength: {} \nCurrent Board:".format(ship.shipName, ship.size))
        player.board.drawBoardShip()
        print("Please enter ship orientation (vertical/horizontal):")
        ship.changeOrientation(input())
        print("Enter the position: ")
        while not player.board.insertShip(ship,int(input())):
            print("Incorrent Input. Enter the position: ")

    print("Final Board:")
    player.board.drawBoardShip()
    print("Press enter to continue:")
    input()
    clear()

# for ship in game.p2.ships:
#     print("Current Player: "+game.p2.name)
#     print("Insert Ship: {} \nLength: {} \nCurrent Board:".format(ship.shipName, ship.size))
#     game.p2.board.drawBoardShip()
#     print("Please enter ship orientation (vertical/horizontal):")
#     ship.changeOrientation(input())
#     print("Enter the position: ")
#     while not game.p2.board.insertShip(ship,int(input())):
#         print("Incorrent Input. Enter the position: ")

# print("Final Board:")
# game.p2.board.drawBoardShip()
# print("Press enter to continue:")
# input()
# clear()


initialiseShips(game.p1)
initialiseShips(game.p2)

