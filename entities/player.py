from config import player_ships
from entities.board import Board
from entities.ship import Ship
from services.ready import playerReady

class Player(object):
    def __init__(self,name):
        self.name = name
        self.ships = []
        for shipType in player_ships:
            for _ in range(player_ships[shipType]):
                self.ships.append(Ship(shipType))
        self.board = Board()
        
    def setOpponent(self,player):
        self.opponent = player
        
    def getPlayerHealth(self):
        health = 0
        for ship in self.ships:
            health += ship.health
        return health