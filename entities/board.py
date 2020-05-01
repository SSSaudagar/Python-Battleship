from config import board_config

class Board(object):
    def __init__(self):
        self.rows = board_config['rows']
        self.columns = board_config['columns']
        self.board = [[['e',None]for j in range(self.columns)] for i in range(self.rows)]
    
    def getRC(self,position):
        row = position//self.columns
        column = position % self.columns
        return row,column
    
    def insertShip(self,ship,position):
        row,column = self.getRC(position)
        currRC = lambda x: [row+x,column] if (ship.orientation) else [row,column+x]
        for i in range(ship.size):
            r,c = currRC(i)
            if r>= self.rows or c>= self.columns:
                for j in range(i):
                    r1,c1 = currRC(j)
                    self.board[r1][c1][1] = None
                print("Ship Out of bounds")
                return False
            elif self.board[r][c][1] != None:
                for j in range(i):
                    r1,c1 = currRC(j)
                    self.board[r1][c1][1] = None
                print("Ship already exists at this position")
                return False
            else:
                self.board[r][c][1] = ship
        return True
                
            
    def attack(self,position):
        r,c = self.getRC(position)
        
        if self.board[r][c][0] == 'e':
            if self.board[r][c][1] is None:
                self.board[r][c][0] = 'm'
                print('Attack Missed')
                return
            else:
                self.board[r][c][0] = 'h'
                print("Ship Hit")
                self.board[r][c][1].hit()
            return True
        else:
            return False
        
    def drawBoardAttack(self):
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if self.board[i][j][0] == 'e':
                    row.append("{0:>2}".format(i*self.columns +j))
                else:
                    row.append(" "+self.board[i][j][0])
            print(" ".join(row))
    
    def drawBoardShip(self):
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if self.board[i][j][1] is None:
                    row.append("{0:>2}".format(i*self.columns +j))
                else:
                    if self.board[i][j][0] == 'e':
                        row.append(' s')
                    else:
                        row.append(' x')
            print(" ".join(row))
        