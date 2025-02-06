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


running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:

    screen.blit(house, (0, 0))
   
   

    # Skriver tekst på skjermen:
    # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)

    # Flytter og tegner spilleren:
    player.draw(screen)
    player.move()

    
    """
    Logikk for bytte bakgrunnsbilde med karakterens koordinat
    
    if self.image == house and self.x == helt til høyre: 
        self.image == nytt bilde
        if self.image == det riktige bildet:  
        vise tilsvarende frukt og tang
        
        gi spilleren en ny posisjon som stemmer med brettet
            - går man ut av huset kan man ikke ende opp i vannet, man må flytte Victor så han er utenfor døren
            - men ikke så nærme at man blir stuck i en evig loop av inne og ute
            - reversere posisjonen? 
        
    
    passe på at visse ting som bær og bjørn skal vises med riktig bakgrunnsbilde
    Sjekke om det finnes måter å animere bytte mellom bilder så det blir smoothere
    """


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()