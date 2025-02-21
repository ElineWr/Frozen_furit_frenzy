import pygame as pg
from button import Button

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


pg.display.set_caption("Meny")



def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)


# food_animasjonsliste = []
# food_animasjons_steps = 4
# food_frame = 0
# food_last_update_time = pg.time.get_ticks()  # Time of last frame update
# food_animation_cooldown = 700  # Milliseconds between frame updates


player = Player(x = WIDTH/2, y = HEIGHT/2, dy = 3, dx = 3, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


# lager animasjons listen
def play(): 
    game = Game()

    food_x = 0  # Default value
    food_y = 0  # Default value
    
    
    food_animasjonsliste = []
    food_animasjons_steps = 4
    food_frame = 0
    food_last_update_time = pg.time.get_ticks()  # Time of last frame update
    food_animation_cooldown = 700  # Milliseconds between frame updates

    for x in range(food_animasjons_steps):
        food_animasjonsliste.append(blaaber_1.get_image(x, width_food = 82.66, height_food=83.66, scale=1, color=BLACK))


    running = True
    while running:
        # try:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
        # except Exception as e:
        #     print(f"Error: {e}")
        #     running = False
                    
        clock.tick(FPS)

        PLAY_MOUSE_POS = pg.mouse.get_pos()

        # screen.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # screen.blit(PLAY_TEXT, PLAY_RECT)


        '''
        Kan bruke denne logikken til å lage en quit knapp i pause-meny
        
        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        '''

        # Tegner bakgrunnsbildet:


        screen.blit(game.backgrounds[0], (0, 0))
        
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


        
        if game.current_background_index == 0:
                food_x = 0
                food_y = 0
        if game.current_background_index == 1:
                food_x = 400
                food_y = 300
                print(f"Food position updated to coast: ({food_x}, {food_y})")
        elif game.current_background_index == 2:
                food_x = 400
                food_y = 300
                print(f"Food position updated to coast: ({food_x}, {food_y})")
        elif game.current_background_index == 3:
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
        


        for square in all_squares: 
            square.tegn(screen, game)
            
            
        pg.display.update()


    # Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
    pg.quit()

def options():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(WIDTH/2, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color=MEDIUM_BLUE)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pg.display.update()


def main_menu():
    while True:
        screen.blit(house, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(50).render("FROZEN FRUIT FRENZY", True, DARK_BLUE)
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, 75))

        PLAY_BUTTON = Button(image=play_rect, pos=(WIDTH/2, 250), 
                            text_input="PLAY", font=get_font(75), base_color=OFFWHITE, hovering_color=DARK_BLUE)
        OPTIONS_BUTTON = Button(image=opt_rect, pos=(WIDTH/2, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color=OFFWHITE, hovering_color=DARK_BLUE)
        QUIT_BUTTON = Button(image=quit_rect, pos=(WIDTH/2, 550), 
                            text_input="QUIT", font=get_font(75), base_color=OFFWHITE, hovering_color=DARK_BLUE)

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    pg.sys.exit()

        pg.display.update()

main_menu()