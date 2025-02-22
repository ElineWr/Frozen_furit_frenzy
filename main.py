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
from game import Game, food_x, food_y
from square_objects import squares, all_squares, Square

food_last_update_time = pg.time.get_ticks()  # Time of last frame update
food_animation_cooldown = 700  # Milliseconds between frame updates


player = Player(x = WIDTH/2, y = HEIGHT/2, dy = 3, dx = 3, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


# lager animasjons listen

game = Game()

def tegne(background):

        if background == 1:
            screen.blit(bjorneber, (550, 600))
            screen.blit(bringeber, (50, 200))
            screen.blit(appelsin, (60, 60))
            #print(f"Food position updated to coast: ({food_x}, {food_y})")
            
            
        elif background == 2:
            screen.blit(bjorneber, (950, 330))
            screen.blit(blaaber, (100, 50))
            screen.blit(bringeber, (150, 610))
            #print(f"Food position updated to coast: ({food_x}, {food_y})")
 
        elif background == 3:

            screen.blit(appelsin, (200, 100))
            screen.blit(blaaber, (300, 400))
            #print(f"Food position updated to coast: ({food_x}, {food_y})")


#for x in range(food_animasjons_steps):
    #food_animasjonsliste.append(Food.get_image(frame = x, width_food = 82.66, height_food=83.66, scale=1, color=BLACK))

player_rect = pg.Rect(player.x, player.y, player.width, player.height)
blaaber_rect = pg.Rect(food_x, food_y, 82.66, 83.66)

running = True
while running:
    #try:
    for event in pg.event.get():
            # if event.type == pg.MOUSEBUTTONDOWN: 
            #     pos = pg.mouse.get_pos()
                
            #     square = Square(BLACK, pos[0], pos[1], 50, 50)
            #     squares.add(square)
        if event.type == pg.QUIT:
            running = False
            # elif event.type == pg.KEYDOWN:
            #     print(f"Key pressed: {event.key}")  # Legg til logging for tastetrykk
    #except Exception as e:
        #print(f"Error: {e}")
        #running = False
                
         

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

        """
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

    """

   
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

 
    #if player_rect.colliderect(blaaber_rect):
        # food_x = 0
       #  player.score += 1
        # print(f"Player collected a blueberry! Current score: {player.score}")

    #blaaber_1.draw(screen, player)

    current_time = pg.time.get_ticks()
    if current_time - food_last_update_time >= food_animation_cooldown:
        food_frame += 1
        food_last_update_time = current_time  # Update the last frame update time
        if food_frame >= food_animasjons_steps:  # Loop the frames
            food_frame = 0

    # Blit the correct frame
    #if change_background(player) != house:
    #screen.blit(food_animasjonsliste[food_frame], (food_x, food_y))

    #for ting in all_ber: 
    tegne(background = game.current_background_index)
        #ting.colisjon_mat(player)

    # #diamant.tegn(screen)
        
    #prøve kolisjon med bilde
    """
    image_width, image_height = 10, 20
    image_x, image_y = 400, 250
    image_rect = pg.Rect(image_x, image_y, image_width, image_height)
    player_rect = pg.Rect(player.x, player.y, player.width, player.height)

    screen.blit(blaaber, image_rect)

    if player_rect.colliderect(image_rect):
        print("Collision detected!")
    """


    for square in all_squares: 
        square.tegn(screen, game)
        
        
    pg.display.update()


# Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
pg.quit()
