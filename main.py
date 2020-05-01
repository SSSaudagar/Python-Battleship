from services.helpers import clearScreen
from services.ready import playGame
from services.initialise import initGame

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
            