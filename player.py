
from objekter import Object
from constants import PLAYER_SPEED, WIDTH, HEIGHT
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *
from player import*

class Player(Object):

    def __init__(self, x, y, dy, image, money, carryingFood):
        super().__init__(x, y, image)
        self.dy = dy
        self.money = money
        self.carryingFood = carryingFood
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def beat(self, x, y, carryingFood):
        pass

    def move(self):
        
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.x = max(self.x - PLAYER_SPEED, self.width)  # Hindrer at x blir mindre enn self.width
        if keys_pressed[K_RIGHT]:
            self.x = min(self.x + PLAYER_SPEED, WIDTH - self.width)  # Hindrer at x går over WIDTH - self.width
        if keys_pressed[K_UP]:
            self.y = max(self.y - PLAYER_SPEED, 0)  # Hindrer at y blir negativ
        if keys_pressed[K_DOWN]:
            self.y = min(self.y + PLAYER_SPEED, HEIGHT - self.height)  # Hindrer at y går over HEIGHT - self.height
            
        
        # if keys_pressed[K_LEFT] and self.x > 0:
        #     self.x -= PLAYER_SPEED
        #     self.image = victor
        # if keys_pressed[K_RIGHT] and self.x < WIDTH:
        #     self.x += PLAYER_SPEED
        # if keys_pressed[K_UP] and self.y > 0:
        #     self.y -= PLAYER_SPEED
        #     self.image = victor
        # if keys_pressed[K_DOWN] and self.y < HEIGHT:
        #     self.y += PLAYER_SPEED
        #     self.image = victor

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
