
from objekter import Object
from constants import PLAYER_SPEED, WIDTH, HEIGHT
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *

class Player(Object):

    def __init__(self, x, y, dy, image, money, carryingFood):
        super().__init__(x, y, image)
        self.dy = dy
        self.money = money
        self.carryingFood = carryingFood

    def beat(self, x, y, carryingFood):
        pass

    def move(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT] and self.x > 0:
            self.x -= PLAYER_SPEED
            # self.image = link_l
        if keys_pressed[K_RIGHT] and self.x < WIDTH:
            # self.x += PLAYER_SPEED
        if keys_pressed[K_UP] and self.y > 0:
            self.y -= PLAYER_SPEED
            # self.image = link_u
        if keys_pressed[K_DOWN] and self.y < HEIGHT:
            self.y += PLAYER_SPEED
            # self.image = link_d

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

