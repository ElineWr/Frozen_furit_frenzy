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


player = Player(x = 100, y = 100, dy = 0, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:
    screen.blit(house, (0, 0))

    # # Skriver tekst på skjermen:
    # # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)

    # # Flytter og tegner spilleren:
    # player.draw(screen)
    # player.move()
    # #diamant.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()