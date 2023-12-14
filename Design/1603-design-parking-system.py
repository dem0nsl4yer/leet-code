class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big >0:
                self.big -= 1
                return True 
            else:
                return False 
        if carType == 2:
            if self.medium >0:
                self.medium -= 1
                return True 
            else:
                return False
        if carType == 3:
            if self.small >0:
                self.small -= 1
                return True
            else:
                return False  
            
# Shorter code

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.spaces.get(carType) > 0:
            self.spaces[carType] -= 1
            return True
        return False