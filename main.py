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
from player import Player
from objekter import *


player = Player(x = 700, y = 220, dy = 1, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)

def get_image(sheet, frame, width_sprite, height_sprite, scale, color):
    image = pg.Surface((width_sprite, height_sprite)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width_sprite), 0, width_sprite, height_sprite))
    image = pg.transform.scale(image, (width_sprite * scale, height_sprite * scale))
    image.set_colorkey(color)

    return image

frame_0 = get_image(victor, frame = 0,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
frame_1 = get_image(victor, frame = 1,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
frame_2 = get_image(victor, frame = 2,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
frame_3 = get_image(victor, frame = 3,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
frame_4 = get_image(victor, frame = 4,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)
frame_5 = get_image(victor, frame = 5,  width_sprite = 90, height_sprite = 115, scale = 1, color = BLACK)

    


running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:
    screen.blit(house, (0, 0))

    screen.blit(frame_0, (0, 0))

    # # Skriver tekst på skjermen:
    # # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)

    # # Flytter og tegner spilleren:
    #player.draw(screen)
    #player.move()
    # #diamant.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()