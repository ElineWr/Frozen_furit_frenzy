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
from game import Game, food_x, food_y
from square_objects import squares, all_squares, Square


# pg.display.set_caption("Meny")

game = Game()  # Opprett et Game-objekt før du starter hovedmenyen

def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)


# food_animasjonsliste = []
# food_animasjons_steps = 4
# food_frame = 0
# food_last_update_time = pg.time.get_ticks()  # Time of last frame update
# food_animation_cooldown = 700  # Milliseconds between frame updates


# legg inn på riktig sted: 
player_rect = pg.Rect(player.x, player.y, player.width, player.height)
blaaber_rect = pg.Rect(food_x, food_y, 82.66, 83.66)

player = Player(x = WIDTH/2, y = HEIGHT/2, dy = 3, dx = 3, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


# lager animasjons listen
def play(game): 
    food_x = 0  # Default value  
    food_y = 0  # Default value
    
    
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

    # Initialiser spill-variabler  
    food_animasjonsliste = []
    food_animasjons_steps = 4  
    food_frame = 0  
    food_last_update_time = pg.time.get_ticks()  # Time of last frame update  
    food_animation_cooldown = 700  # Milliseconds between frame updates

    for x in range(food_animasjons_steps):
        food_animasjonsliste.append(blaaber_1.get_image(x, width_food = 82.66, height_food=83.66, scale=1, color=BLACK))

    running = True  
    while running:
        clock.tick(FPS)

        PLAY_MOUSE_POS = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False  
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    print("M-knappen ble trykket!")
                    main_menu(game)
                    # Her kan du legge til en enkel melding eller noe annet for å bekrefte  

        
        screen.blit(game.backgrounds[game.current_background_index], (0, 0))


        # Oppdater spilllogikk  
        player.draw(screen)
        keys_pressed = pg.key.get_pressed()
        if not any(keys_pressed):  # If no keys are pressed  
            frame = 0  
        else:
            for square in squares:
                if square.background == game.current_background_index:      
                    square.detect_collision(player, game)
            player.move(squares, game)

        # Oppdater matposisjon basert på bakgrunn  
        if game.current_background_index == 0:
            food_x = 0  
            food_y = 0  
        elif game.current_background_index in [1, 2, 3]:
            food_x = 400  
            food_y = 300
            
         #if player_rect.colliderect(blaaber_rect):
        # food_x = 0
       #  player.score += 1
        # print(f"Player collected a blueberry! Current score: {player.score}")
            
        # if player.x >= WIDTH - player.width:  # Høyre kant  
        #     game.change_background(player)
        # elif player.x <= 0:  # Venstre kant  
        #     game.change_background(player)
        # elif player.y <= 0:  # Toppkant  
        #     game.change_background(player)
        # elif player.y >= HEIGHT - player.height:  # Bunnkant  
        #     game.change_background(player)


        # Mat animasjon  
        current_time = pg.time.get_ticks()
        if current_time - food_last_update_time >= food_animation_cooldown:
            food_frame += 1  
            food_last_update_time = current_time  # Update the last frame update time  
            if food_frame >= food_animasjons_steps:  # Loop the frames  
                food_frame = 0

        screen.blit(food_animasjonsliste[food_frame], (food_x, food_y))

        # Tegn spillobjekter  
        for square in all_squares: 
            square.tegn(screen, game)
            
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
            
            
    

    # Brukeren har avsluttet programmet, game-loopen er ferdig. Avslutt pygame:
    # Men når denne er blokkert så kan man bruke avsluttknappen til bildet som en tilbake til meny-knapp
    #  pg.quit()

def game_info(game):
    current_background_index = game.current_background_index  # Behold den nåværende bakgrunnen

    while True:
        INFO_MOUSE_POS = pg.mouse.get_pos()


        # screen.blit(game.backgrounds[current_background_index], (0, 0))  # Bruk den lagrede bakgrunnen
        screen.fill(WHITE)

        INFO_HEADER = get_font(26).render("Her er info om hvordan spillet funker", True, BLACK)
        HEADER_RECT = INFO_HEADER.get_rect(center=(WIDTH/2, 80))
        screen.blit(INFO_HEADER, HEADER_RECT)

        screen.blit(victor_info, (WIDTH/2 - 50, 125))

        INFO_TEXT_LINES = ["Victor har fått et viktig oppdrag:",
                           "Han må samle spesifikke bær i det",
                           "iskalde vinterlandskapet.",
                           "Følg instruksene nøye og ha det gøy",
                           "mens du navigerer snø og hindringer",
                           "for å hente bærene."]

        y_offset = 300  # Startposisjon for teksten  
        for line in INFO_TEXT_LINES:
            text_surface = get_font(20).render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH/2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30  # Øk y-posisjonen for neste linje

        KEYS_TXT = get_font(20).render("Bruk piltastene til å navigere Victor", True, BLACK)
        KEYS_RECT = KEYS_TXT.get_rect(center=(WIDTH/2, 500))
        screen.blit(KEYS_TXT, KEYS_RECT)

        EXIT = get_font(20).render("Bruk esc for å komme tilbake til hovedmeny", True, BLACK)
        EXIT_RECT = EXIT.get_rect(center = (WIDTH/2, 600))
        screen.blit(EXIT, EXIT_RECT)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:  # Bruk escape-tasten for å gå tilbake  
                    return  # Gå tilbake til den forrige skjermen

        pg.display.update()

def main_menu(game):
    
    while True:
        screen.blit(game.backgrounds[game.current_background_index], (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(50).render("FROZEN FRUIT FRENZY", True, OFFWHITE)
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, 75))
        
        BACK_TO = get_font(20).render("Trykk på M for å åpne menyen", True, DARK_BLUE)
        BACK_RECT = BACK_TO.get_rect(center = (WIDTH/2, 660))
        
        MENU_BCK = Button(image = menu_bck, pos=(WIDTH/2, 75), 
                          text_input="", font=get_font(75), base_color=OFFWHITE, hovering_color=DARK_BLUE)

        PLAY_BUTTON = Button(image=play_rect, pos=(WIDTH/2, 250), 
                            text_input="PLAY", font=get_font(75), base_color=OFFWHITE, hovering_color=DARK_BLUE)
        INFO_BUTTON = Button(image=info_rect, pos=(WIDTH/2, 400), 
                            text_input="GAME INFO", font=get_font(60), base_color=OFFWHITE, hovering_color=DARK_BLUE)
        QUIT_BUTTON = Button(image=quit_rect, pos=(WIDTH/2, 550), 
                            text_input="QUIT", font=get_font(75), base_color=OFFWHITE, hovering_color=DARK_BLUE)



        for button in [PLAY_BUTTON, INFO_BUTTON, QUIT_BUTTON, MENU_BCK]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(BACK_TO, BACK_RECT)
        
        # for event in pg.event.get():
        #     if event.type == pg.QUIT:
        #         pg.quit()
        #         quit()
        #     if event.type == pg.MOUSEBUTTONDOWN:
        #         if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
        #             play(game)  # Send game object to play function
        #         if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
        #             game_info(game)
        #         if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
        #             pg.quit()
        #             pg.sys.exit()
        #     if event.type == pg.KEYDOWN: 
        #         if event.key == pg.K_m:  # Hvis "M" trykkes  
        #             main_menu(game)  # Gå til hovedmenyen
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(game)  # Send game object to play function
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_info(game)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    pg.sys.exit()

        pg.display.update()


main_menu(game)