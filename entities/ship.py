from config import ship_config

class Ship(object):
    
    def __init__(self, shipType):
        
        self.shipName = shipType.capitalize()
        self.size = ship_config[shipType]
        self.health = ship_config[shipType]
        self.orientation = 0
        self.status = 1
        
    def changeOrientation(self,orientation):
        if orientation[0].capitalize() == "V":
            self.orientation = 1
        elif orientation[0].capitalize() == "H":
            self.orientation = 0
        else:
            print("Incorrect Orientation: Orientation could not be changed. Current orientation is {}".format("vertical" if self.orientation else "horizontal"))
            return False
        return True
    
    def hit(self):
        self.health -=1
        if self.health == 0:
            self.status = 0
            print("Ship {} sunk".format(self.shipName))