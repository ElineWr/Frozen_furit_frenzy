import pygame as pg
from constants import * 
from bilder import*



class Game(): 
    def __init__(self): 
        self.backgrounds = [house, coast, camp, cave]
        self.current_background_index = 0
        self.background = self.backgrounds[self.current_background_index]

            
    def change_background(self, player):
    # Bytt bakgrunn basert på spillerens posisjon  
        if self.current_background_index == 0 and player.x >= WIDTH - player.width:  
            self.current_background_index = 1  
            player.x = 10  
            
        elif self.current_background_index == 1 and player.x <= 0:  
            self.current_background_index = 0  
            player.x = WIDTH - 10 - player.width  

            
        elif self.current_background_index == 1 and player.y <= 0: 
            self.current_background_index = 2  
            player.y = HEIGHT - player.height - 10  

            
        elif self.current_background_index == 2 and player.y <= 0: 
            self.current_background_index = 3  
            player.y = HEIGHT - player.height - 10 

            
        elif self.current_background_index == 3 and player.y >= HEIGHT - player.height:
            self.current_background_index = 2  
            player.y = 10  

            
        elif self.current_background_index == 2 and player.y >= HEIGHT - player.height:
            self.current_background_index = 1  
            player.y = 10

        
        self.background = self.backgrounds[self.current_background_index]
            
    def draw_background(self, screen):
        screen.blit(self.background, (0, 0))  # Tegn den nåværende bakgrunnen
        
    

