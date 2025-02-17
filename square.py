import pygame as pg
from constants import *

class Square(pg.sprite.Sprite): 
    def __init__(self, farge, x, y, width, height, ): 
        pg.sprite.Sprite.__init__(self)
        self.farge = farge
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def tegn(self, screen):
       pg.draw.rect(screen, self.farge, (self.x, self.y, self.width, self.height))

         
        
    def update(self): 
        self.y += 5
        
    def detect_collision(self, player):
        """Hindrer spilleren i å gå gjennom firkanten uten å bruke rect."""
        if (player.x < self.x + self.width and 
            player.x + player.width > self.x and 
            player.y < self.y + self.height and 
            player.y + player.height > self.y):

            # Stopp spilleren avhengig av retning
            if player.dx > 0:  # Går til høyre
                player.x = self.x - player.width
            elif player.dx < 0:  # Går til venstre
                player.x = self.x + self.width
            if player.dy > 0:  # Går nedover
                player.y = self.y - player.height
            elif player.dy < 0:  # Går oppover
                player.y = self.y + self.height

        


square = Square(BLACK, 100, 100, 50, 50)
squares = pg.sprite.Group()
squares.add(square)

