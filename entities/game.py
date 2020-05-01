from entities.player import Player
class Game(object):
    def __init__(self,player1,player2):
        self.p1 = Player(player1)
        self.p2 = Player(player2)
        self.state = 0
        self.curr = self.p1
        self.p1.setOpponent(self.p2)
        self.p2.setOpponent(self.p1)

    # def isGameOver(self):
    #     return self.p1.getPlayerHealth() == 0 or self.p2.getPlayerHealth() == 0

    def winner(self):
        if self.p1.getPlayerHealth() == 0:
            return self.p2.name
        elif self.p1.getPlayerHealth() == 0:
            return self.p1.name
        else:
            return False
    
    def changeCurrentPlayer(self):
        if self.curr == self.p1:
            self.curr = self.p2
        else:
            self.curr = self.p1
