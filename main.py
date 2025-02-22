import pygame as pg  
from constants import *

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)

from button import Button  

from bilder import *
from player import *
from objekter import *
from game import Game, food_x, food_y  
from square_objects import squares, all_squares, Square

# Start opp PyGame:




game = Game()  # Opprett et Game-objekt før du starter hovedmenyen

def get_font(size):  # Returner font i ønsket størrelse  
    return pg.font.Font("assets/font.ttf", size)

# Opprett spilleren  
player = Player(x=WIDTH/2, y=HEIGHT/2, dy=3, dx=3, image=victor, money=0, carryingFood=False)

# Initialiser matvariabler  
food_x = 0  
food_y = 0  
food_animasjonsliste = []
food_animasjons_steps = 4  
food_frame = 0  
food_last_update_time = pg.time.get_ticks()  # Tid for siste oppdatering av ramme  
food_animation_cooldown = 700  # Millisekunder mellom rammeoppdateringer

def play(game):

    def tegne(current_background_index):
        if current_background_index == 1:
            screen.blit(bjorneber, (550, 600))
            screen.blit(bringeber, (50, 200))
            screen.blit(appelsin, (60, 60))
        elif current_background_index == 2:
            screen.blit(bjorneber, (950, 330))
            screen.blit(blaaber, (100, 50))
            screen.blit(bringeber, (150, 610))
        elif current_background_index == 3:
            screen.blit(appelsin, (200, 100))
            screen.blit(blaaber, (300, 400))
            
    global food_last_update_time  # Fortell Python at vi vil bruke den globale variabelen  
    global food_frame  # Hvis du også bruker food_frame, legg til dette  
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

        # Tegn bakgrunn  
        screen.blit(game.backgrounds[game.current_background_index], (0, 0))

        # Oppdater spilleren  
        player.draw(screen)

        keys_pressed = pg.key.get_pressed()
        if not any(keys_pressed):
            frame = 0  
        else:
            for square in squares:
                if square.background == game.current_background_index:
                    square.detect_collision(player, game)
                    
            for berry in all_ber: 
                if berry.background == game.current_background_index:
                    berry.detect_collision_with_food(player, game, all_ber)
                    #player.carryingFood = berry  # Sett bæret som det nåværende 
                    #berry.x = player.x + 10  # Plasser bæret nær spilleren  
                    #berry.y = player.y + 10
                    print(player.carryingFood)
            player.move(squares, game)

                    

        # Mat animasjon  
        current_time = pg.time.get_ticks()
        if current_time - food_last_update_time > food_animation_cooldown:
            food_frame = (food_frame + 1) % food_animasjons_steps  
            food_last_update_time = current_time

        # Oppdater matposisjon basert på bakgrunn  
        # if game.current_background_index == 0:
        #     food_x = 0  
        #     food_y = 0  
        # elif game.current_background_index in [1, 2, 3]:
        #     food_x = 400  
        #     food_y = 300

        # Tegn mat basert på bakgrunn 
      
        tegne(game.current_background_index)
        
        def tegne(current_background_index):
            
            for berry in all_ber:  # Tegn alle bær  
                if player.carryingFood == berry:
                    berry.background = current_background_index
                if berry.background == current_background_index and not berry.is_collected:
                    screen.blit(berry.image, (berry.x, berry.y))

        # Oppdater skjermen  
        pg.display.update()
        
    play(game)

# Avslutt Pygame  

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

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                # pg.sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Play button pressed!")  # Debug
                    play(game)
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_info(game)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    # pg.sys.exit()

        pg.display.update()


main_menu(game)