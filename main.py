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


food_animasjonsliste = []
food_animasjons_steps = 4
food_frame = 0
food_last_update_time = pg.time.get_ticks()  # Time of last frame update
food_animation_cooldown = 700  # Milliseconds between frame updates

food_x = 0  # Default value
food_y = 0  # Default value

for x in range(food_animasjons_steps):
      food_animasjonsliste.append(blaaber_1.get_image(x, width_food = 82.66, height_food=83.66, scale=1, color=BLACK))



running = True
while running:

    # Sjekk om brukeren avslutter vinduet:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
                

    clock.tick(FPS)

    # Tegner bakgrunnsbildet:

    screen.blit(background[0], (0, 0))
    if player.x >= WIDTH - player.width:  # Høyre kant
        change_background(player)
        print(f"Current Background Index: {current_background_index}")
    elif player.x <= 0:  # Venstre kant
        change_background(player)
        print(f"Current Background Index: {current_background_index}")
    elif player.y <= 0: 
        change_background(player)
        print(f"Current Background Index: {current_background_index}")
    elif player.y >= HEIGHT - player.height:
        change_background(player)
        print(f"Current Background Index: {current_background_index}")

    
   

    # Skriver tekst på skjermen:
    # TODO: Skriv inn scoren som en tekst øverst på skjermen (bruk aunivers)

    # Flytter og tegner spilleren:
    player.draw(screen)


    keys_pressed = pg.key.get_pressed()
    if not any(keys_pressed):  # If no keys are pressed
            frame = 0
    else:
        player.move()

    
    #if change_background(player) == house:
            #food_x = 0
            #food_y = 0
    if backgrounds[0] == coast:
            food_x = 400
            food_y = 300
            print(f"Food position updated to coast: ({food_x}, {food_y})")
    elif backgrounds[0] == camp:
            food_x = 400
            food_y = 300
            print(f"Food position updated to coast: ({food_x}, {food_y})")
    elif backgrounds[0] == cave:
            food_x = 400
            food_y = 300
            print(f"Food position updated to coast: ({food_x}, {food_y})")
    
    
    #blaaber_1.draw(screen, player)

    current_time = pg.time.get_ticks()
    if current_time - food_last_update_time >= food_animation_cooldown:
        food_frame += 1
        food_last_update_time = current_time  # Update the last frame update time
        if food_frame >= food_animasjons_steps:  # Loop the frames
            food_frame = 0

    # Blit the correct frame
    #if change_background(player) != house:
    screen.blit(food_animasjonsliste[food_frame], (food_x, food_y))
    

    # #diamant.tegn(screen)


    # Oppdater skjermen for å vise endringene:
    pg.display.update()

# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
