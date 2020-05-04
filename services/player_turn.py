from services.helpers import clearScreen

def playerTurn(game):
    print("Current Player: {}".format(game.curr.name))
    print("Player Health: {}".format(game.curr.getPlayerHealth()))
    print("Your Ship Board:")
    game.curr.board.drawBoardShip()
    print("Attack Board:")
    game.curr.opponent.board.drawBoardAttack()
    while True:
        try:
            attack = int(input("Enter the position to attack:"))      
            message = game.curr.opponent.board.attack(attack)
        except TypeError:
            print("Please enter valid position.")
        except ValueError as err:
            print("Invalid Input. ",err)
        except:
            print("Oops Something went wrong")
        else:
            clearScreen()
            print(message)
            game.changeCurrentPlayer()
            return
        
    