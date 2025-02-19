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
        pass
        # if self.background == game.current_background_index:
        #     pg.draw.rect(screen, self.farge, (self.x, self.y, self.width, self.height))
            
    # def update(self): 
    #     self.y += 5
        
    def detect_collision(self, player, game):
        player_rect = pg.Rect(player.x, player.y, player.width, player.height)
        square_rect = pg.Rect(self.x, self.y, self.width, self.height)
        
        if self.background != game.current_background_index:
            return False  # Ingen kollisjon hvis bakgrunnen ikke stemmer
        if player_rect.colliderect(square_rect):
        # Behandle kollisjon her  
        # Finn ut hvilken side spilleren kolliderte med  
            if abs(player_rect.top - square_rect.bottom) < 10:  # Kolliderer med bunnen av firkanten  
                player.y = square_rect.top - player.height  
            elif abs(player_rect.bottom - square_rect.top) < 10:  # Kolliderer med toppen av firkanten  
                player.y = square_rect.bottom  
            elif abs(player_rect.right - square_rect.left) < 10:  # Kolliderer med venstre side av firkanten  
                player.x = square_rect.left - player.width  
            elif abs(player_rect.left - square_rect.right) < 10:  # Kolliderer med høyre side av firkanten  
                player.x = square_rect.right

            return True  # Kollisjon oppstod  
        return False  # Ingen kollisjon

        
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
    Square(farge = BLACK, x = 0, y = 0, width = WIDTH*(6/10), height= 50, background = 2),
    Square(farge = BLACK, x = 0, y = HEIGHT*(7/10), width = 150, height=150, background = 2),
    Square(farge = BLACK, x = 250, y = HEIGHT*(8/10), width = 100, height = 100, background = 2),
    
    # coast
    Square(farge = BLACK, x = 0, y = 0, width=150, height=300, background=3),
    Square(farge = BLACK, x = 0, y = HEIGHT - 400, width=50, height=400, background=3),
    Square(farge = BLACK, x = 0, y = HEIGHT - 100, width=WIDTH*(5/10), height=100, background=3),
    Square(farge = BLACK, x = WIDTH*(5/10), y = HEIGHT*(2/10), width=200, height=260, background=3),
    Square(farge = BLACK, x = 0, y = 0, width = WIDTH*(4.5/10), height=75, background=3),
    Square(farge = BLACK, x = 0, y = HEIGHT-100, width=WIDTH*(5/10), height=100, background=3),

]
squares = pg.sprite.Group()
squares.add(all_squares)




