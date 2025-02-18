import pygame as pg
from constants import *
# from functions import *
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
        player_rect = pg.Rect(player.x, player.y, player.width, player.height)
        square_rect = pg.Rect(self.x, self.y, self.width, self.height)
    
        if player_rect.colliderect(square_rect):
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
    Square(farge=BLACK, x=0, y=0, width=250, height=HEIGHT, background=0),
    Square(farge = BLACK, x = WIDTH - 50, y = 0, width = 50, height = (HEIGHT*(4/8)), background = 0),
    Square(farge = BLACK, x = WIDTH - 50, y = (HEIGHT*(6/8)), width = 50, height = (HEIGHT*(2/8)), background = 0),
    Square(farge = BLACK, x = 0, y = 0, width = WIDTH, height = (HEIGHT*(1.5/8)), background = 0),
    Square(farge = BLACK, x = 0, y = HEIGHT - (HEIGHT*(1/8)), width = WIDTH, height = (HEIGHT*(1/8)), background = 0),
    
    # Square(farge = BLACK, x = 0, y = HEIGHT - , width = 50, height = (HEIGHT*(4/8)), background = 0),
    # coast
    Square(farge=RED, x=0, y=0, width=WIDTH*(1/10), height=HEIGHT*(5/10), background=1),
    
    # camp
    Square(farge = BLACK, x = 0, y = 0, width = WIDTH*(6/10), height= 50, background=2),
    # coast
    Square(farge = BLACK, x= 0, y = 0, width=150, height=300, background=3),
    Square(farge = BLACK, x= 0, y = HEIGHT - 400, width=50, height=400, background=3),
    Square(farge = BLACK, x= 0, y = HEIGHT - 100, width=WIDTH*(5/10), height=100, background=3),
    Square(farge = BLACK, x = WIDTH*(5/10), y = HEIGHT*(2/10), width=200, height=300, background=3)

]


squares = pg.sprite.Group()
squares.add(all_squares)



