
from objekter import Object
from constants import PLAYER_SPEED

class Player(Object):

    def __init__(self, x, y, dy, image, money, carryingFood):
        super().__init__(x, y, image)
        self.dy = dy
        self.money = money
        self.carryingFood = False
