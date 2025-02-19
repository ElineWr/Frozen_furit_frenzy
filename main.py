import pygame as pg

# Start opp PyGame:
pg.init()

from constants import *

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)

# Henter inn tekst, bilder, og spilleren:
# Merk: Kan ikke laste inn font og bilder før vi har gjort pg.init:
#from tekst import *
from bilder import *
from player import *
from objekter import *
from game import Game
from square_objects import squares, all_squares


player = Player(x = WIDTH/2, y = HEIGHT/2, dy = 3, dx = 3, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


# lager animasjons listen

game = Game()

running = True
while running:
    try:
        for event in pg.event.get():
            # if event.type == pg.MOUSEBUTTONDOWN: 
            #     pos = pg.mouse.get_pos()
                
            #     square = Square(BLACK, pos[0], pos[1], 50, 50)
            #     squares.add(square)
            if event.type == pg.QUIT:
                running = False
            # elif event.type == pg.KEYDOWN:
            #     print(f"Key pressed: {event.key}")  # Legg til logging for tastetrykk
    except Exception as e:
        print(f"Error: {e}")
        running = False
                

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:

    # screen.blit(background[0], (0, 0))
    
    if player.x >= WIDTH - player.width:  # Høyre kant  
        game.change_background(player)
    elif player.x <= 0:  # Venstre kant  
        game.change_background(player)
    elif player.y <= 0:  # Toppkant  
        game.change_background(player)
    elif player.y >= HEIGHT - player.height:  # Bunnkant  
        game.change_background(player)
   
    # Skriver tekst på skjermen:

    game.draw_background(screen)
    # Flytter og tegner spilleren:
    player.draw(screen)


    keys_pressed = pg.key.get_pressed()
    if not any(keys_pressed):  # If no keys are pressed
            frame = 0
    else:
        for square in squares:
            if square.background == game.current_background_index:      
                square.detect_collision(player, game)
        player.move(squares, game)


    for square in all_squares: 
        square.tegn(screen, game)
        
        
    pg.display.update()


# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
