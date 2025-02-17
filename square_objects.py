import pygame as pg
from constants import *
from functions import *
from game import Game



class Square(pg.sprite.Sprite): 
    def __init__(self, farge, x, y, width, height, background): 
        pg.sprite.Sprite.__init__(self)
        self.farge = farge
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = background 

    
    def tegn(self, screen, game):  # Legg til current_background som parameter
        if self.background == game.current_background_index:
            pg.draw.rect(screen, self.farge, (self.x, self.y, self.width, self.height))
            
    # def update(self): 
    #     self.y += 5
        
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

        


all_squares = [
    # house 
    Square(farge=BLACK, x=50, y=50, width=100, height=100, background=0),
    
    # coast
    Square(farge=RED, x=200, y=150, width=100, height=100, background=1),
    # camp
    Square(farge=GREEN, x=300, y=100, width=100, height=100, background=2),
    
    # cave
    Square(farge=BLUE, x=400, y=200, width=100, height=100, background=3)
]


squares = pg.sprite.Group()
squares.add(all_squares)



