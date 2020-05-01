from entities.game import Game
from services.initialise import initialiseShips
from services.helpers import clearScreen

clearScreen()

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")

game = Game(player1,player2)

initialiseShips(game.p1)
initialiseShips(game.p2)

