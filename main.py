from entities.game import Game
from services.initialise import initialiseShips, initPlayer
from services.helpers import clearScreen
from services.ready import playerReady
from services.player_turn import playerTurn


def playGame(game):
    while not game.winner():
        playerReady(game)
        playerTurn(game)

    if game.winner():    
        print("Game Completed. {} is the winner".format(game.winner()))
    else:
        print("Game not Complete")
    input("Press Enter to exit . . .")

def initGame():
    clearScreen()
    player1 = input("Enter Player 1 Name: ")
    player2 = input("Enter Player 2 Name: ")
    game = Game(player1,player2)
    clearScreen()
    initPlayer(game)
    initPlayer(game)
    return game

games = []
while True:
    clearScreen()
    print("*************************")
    print("* Welcome to Battleship *")
    print("*************************")

    print("\nMake a choice. Type exit to exit")
    print("0 : New Game")
    for i in range(len(games)):
        print("{} : {}".format(i+1,games[i]))
    
    choice = input("Enter choice: ")
    if choice == "exit":
        break
    try:
        choice = int(choice)
        if choice:
            playGame(games[choice-1])
        else:
            game = initGame()
            games.append(game)
            playGame(game)
    except:
        pass
            
        





