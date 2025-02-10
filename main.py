import pygame as pg
from constants import *
from random import randint


# Start opp PyGame:
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)

# Henter inn tekst, bilder, og spilleren:
# Merk: Kan ikke laste inn font og bilder før vi har gjort pg.init:
#from tekst import *
from bilder import *
from player import *
from objekter import *



player = Player(x = 700, y = 220, dy = 1, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


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

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
                

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:
    screen.blit(house, (0, 0))

    # Oppdader animasjonen
    """
    naatid = pg.time.get_ticks()
    if naatid - siste_oppdadering >= animasjon_cooldown:
        frame += 1
        siste_oppdadering = naatid
        if frame >= len(animasjons_liste[handling]):
            frame = 0

    """



    """
    for x in range(animasjon_steps):
        screen.blit(animasjons_liste[x], (x*72, 0))
    """
    """
    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (100, 0))
    screen.blit(frame_2, (200, 0))
    screen.blit(frame_3, (300, 0))
    screen.blit(frame_4, (400, 0))
    """

    # # Skriver tekst på skjermen:
    # # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)

    # # Flytter og tegner spilleren:
    player.draw(screen)


    keys_pressed = pg.key.get_pressed()
    if not any(keys_pressed):  # If no keys are pressed
            frame = 0
    else:
        player.move()

    # #diamant.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()