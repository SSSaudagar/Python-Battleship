from config import board_config

class Board(object):
    def __init__(self):
        self.rows = board_config['rows']
        self.columns = board_config['columns']
        self.board = [[['e',None]for j in range(self.columns)] for i in range(self.rows)]
    
    def getRC(self,position):
        row = position//self.columns
        column = position % self.columns
        if row >=self.rows:
            raise ValueError("Position out of bounds")
        return row,column
    
    def insertShip(self,ship,position):
        try:
            position = int(position)
            row,column = self.getRC(position)
        except:
            print("Incorrect Input.")
            return False
        currRC = lambda x: [row+x,column] if (ship.orientation) else [row,column+x]
        def reset(x):
            for j in range(x):
                r1,c1 = currRC(j)
                self.board[r1][c1][1] = None
        for i in range(ship.size):
            r,c = currRC(i)
            try:
                if r>= self.rows or c>= self.columns:
                    raise ValueError("Ship Out of bounds")
                elif self.board[r][c][1] != None:
                    raise ValueError("Ship already exists at this position")
                else:
                    self.board[r][c][1] = ship
            except ValueError as err:
                reset(i)
                print("Incorrect Input. ",err)
                return False
        return True
                
            
    def attack(self,position):
        r,c = self.getRC(position)
        
        if self.board[r][c][0] == 'e':
            if self.board[r][c][1] is None:
                self.board[r][c][0] = 'm'
                return 'Attack Missed at position {}'.format(position)
            else:
                self.board[r][c][0] = 'h'
                self.board[r][c][1].hit()
                return "Ship Hit at position {}".format(position)
                
            return True
        else:
            raise ValueError("Position already attacked")
        
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
        