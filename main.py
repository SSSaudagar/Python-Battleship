from entities.game import Game
from services.initialise import initialiseShips, initPlayer
from services.helpers import clearScreen
from services.ready import playerReady
from services.player_turn import playerTurn

clearScreen()
player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")
game = Game(player1,player2)
clearScreen()

initPlayer(game)
initPlayer(game)


while not game.winner():
    playerTurn(game)
    
print("{} is the winner".format(game.winner()))
