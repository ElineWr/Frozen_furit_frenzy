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
from functions import *




player = Player(x = WIDTH/2, y = HEIGHT/2, dy = 1, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


# lager animasjons listen



"""
    frame_0 = sprite_sheet.get_image( frame = 0,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
    frame_1 = sprite_sheet.get_image( frame = 1,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
    frame_2 = sprite_sheet.get_image( frame = 2,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
    frame_3 = sprite_sheet.get_image( frame = 3,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
    frame_4 = sprite_sheet.get_image( frame = 4,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
    frame_5 = sprite_sheet.get_image( frame = 5,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
 """



"""
handling = 1
siste_oppdadering = pg.time.get_ticks()
animasjon_cooldown = 500
frame = 0
"""

running = True
while running:
    try:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                print(f"Key pressed: {event.key}")  # Legg til logging for tastetrykk
    except Exception as e:
        print(f"Error: {e}")
        running = False
                

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:

    screen.blit(background[0], (0, 0))
    if player.x >= WIDTH - player.width:  # Høyre kant
        change_background(player)
        print(player.x)
    elif player.x <= 0:  # Venstre kant
        change_background(player)
    elif player.y <= 0: 
        change_background(player)
    elif player.y >= HEIGHT - player.height:
        change_background(player)
      
   

    # Skriver tekst på skjermen:
    # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)

    # Flytter og tegner spilleren:
    player.draw(screen)


    keys_pressed = pg.key.get_pressed()
    if not any(keys_pressed):  # If no keys are pressed
            frame = 0
    else:
        player.move()

    print(player.width)
    # #diamant.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
