import pygame as pg  
from constants import *

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)

from button import Button  

from bilder import *
from player import *
from objekter import *
from game import Game
from square_objects import squares

# Start opp PyGame:



game = Game()  # Opprett et Game-objekt før du starter hovedmenyen

def get_font(size):  
    return pg.font.Font("assets/font.ttf", size)

 
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
    
    def tegn(current_background_index):
        """
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
        """
        for berry in all_ber: 
            if player.carryingFood == berry:
                berry.background = current_background_index
                berry.x = player.x + 10  
                berry.y = player.y + 10 

            if berry.background == 0 and player.carryingFood:
                player.carryingFood.is_collected = False  #
                player.carryingFood = None  
                if berry.image == blaaber:
                    print("Victor har plukket opp blåbær")
                    player.food_count.update({"blaaber": "Done"})
                elif berry.image == appelsin:
                    print("Victor har plukket opp appelsin")
                    player.food_count.update({"appelsin": "Done"})
                elif berry.image == bringeber:
                    print("Victor har plukket opp bringebær")
                    player.food_count.update({"bringebær": "Done"})
                elif berry.image == bjorneber:
                    print("Victor har plukket opp bjørnebær")
                    player.food_count.update({"bjorneber": "Done"})
                all_ber.remove(berry)

                        #eturn False

            elif berry.background == current_background_index:
                screen.blit(berry.image, (berry.x, berry.y))
    
    global food_last_update_time  
    global food_frame 
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
                if event.key == pg.K_i: 
                    show_inventory(player)

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
                    print(player.carryingFood)
            player.move(squares, game)

                    

        # Mat animasjon  
        current_time = pg.time.get_ticks()
        if current_time - food_last_update_time > food_animation_cooldown:
            food_frame = (food_frame + 1) % food_animasjons_steps  
            food_last_update_time = current_time


      
        tegn(game.current_background_index)
    

 
        pg.display.update()
        

    pg.quit()

def game_info(game):

    while True:

        INFO_MOUSE_POS = pg.mouse.get_pos()
        screen.fill(WHITE)

        INFO_HEADER = get_font(26).render("Her er info om hvordan spillet funker", True, BLACK)
        HEADER_RECT = INFO_HEADER.get_rect(center=(WIDTH/2, 80))
        screen.blit(INFO_HEADER, HEADER_RECT)

        screen.blit(victor_info, (WIDTH/2 - 50, 125))

        INFO_TEXT_LINES = ["Victor har fått et viktig oppdrag:",
                           "Han må samle spesifikke bær i det",
                           "iskalde vinterlandskapet.",
                           "Følg instruksene fra oppgaven nøye og ha det gøy",
                           "mens du navigerer snø og hindringer",
                           "for å hente bærene med hjem."]

        y_offset = 300  # Startposisjon for teksten  
        for line in INFO_TEXT_LINES:
            text_surface = get_font(20).render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH/2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 30  # Øk y-posisjonen for neste linje

        KEYS_TXT = get_font(20).render("Bruk piltastene for å navigere Victor,", True, BLACK)
        KEYS_RECT = KEYS_TXT.get_rect(center=(WIDTH/2, 500))
        screen.blit(KEYS_TXT, KEYS_RECT)
        
        INVENTORY_TXT = get_font(20).render("tasten I viser oppgaven og inventaret ditt", True, BLACK)
        INVENTORY_RECT = INVENTORY_TXT.get_rect(center=(WIDTH/2, 550))
        screen.blit(INVENTORY_TXT, INVENTORY_RECT)
        
        EXIT = get_font(20).render("og esc tar deg tilbake til hovedmenyen.", True, BLACK)
        EXIT_RECT = EXIT.get_rect(center = (WIDTH/2, 600))
        screen.blit(EXIT, EXIT_RECT)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: 
                    return 
        pg.display.update()
        
def show_inventory(player):
    inventory_open = True 

    while inventory_open:  
        
        screen.blit(offwhite_bg, ((WIDTH - 803)/2, (HEIGHT - 410)/2))
        
        # Tegn overskrifter  
        inventory_header = get_font(30).render("Oppgave", True, DARK_BLUE)
        screen.blit(inventory_header, (WIDTH * (1/4) - inventory_header.get_width() / 2, 200))

        task_header = get_font(30).render("Inventar", True, DARK_BLUE)
        screen.blit(task_header, (WIDTH * (2.7/4) - task_header.get_width() / 2, 200))


        tasks = {
        "blaaber": 1,      
        "bjorneber": 1,    
        "bringebær": 1,    
        "appelsin": 1     
    }
        y_offset = 300  # Startposisjon for oppgavene  
        for food_name, required_count in tasks.items():
            food_image = None  
            if food_name == "blaaber":
                food_image = blaaber  
            elif food_name == "bjorneber":
                food_image = bjorneber  
            elif food_name == "bringebær":
                food_image = bringeber  
            elif food_name == "appelsin":
                food_image = appelsin
            
            # Tegn bilde av bæret  
            if food_image:
                food_surface = pg.transform.scale(food_image, (70, 70))  # Skalerer bæret
                screen.blit(food_surface, (WIDTH * (0.6/4), y_offset - 20)) 

            # Tegn antallet ved siden av  
            count_text = get_font(30).render(f"x {required_count}", True, DARK_BLUE)
            screen.blit(count_text, (WIDTH * (0.7/4) + 80, y_offset))  # Plasser antallet til høyre for bæret

            y_offset += 50 
       
        y_offset = 300 
        for food_name, count in player.food_count.items():
            food_image = None  
            if food_name == "blaaber":
                food_image = blaaber  
            elif food_name == "bjorneber":
                food_image = bjorneber  
            elif food_name == "bringebær":
                food_image = bringeber  
            elif food_name == "appelsin":
                food_image = appelsin
            
    
            if food_image:
                food_surface = pg.transform.scale(food_image, (70, 70)) 
                screen.blit(food_surface, (WIDTH*(2.2/4), y_offset - 20))  

            
            count_text = get_font(30).render(f"x {count}", True, DARK_BLUE)
            screen.blit(count_text, (WIDTH*(2.7/4), y_offset)) 

            y_offset += 50 

        all_done = all(value == "Done" for value in player.food_count.values())

        if all_done:
    
            HAPPY_VICTOR = get_font(16).render("Yes! Du er ferdig, nå er Victor glad og mett!", True, DARK_BLUE)
            HAPPY_RECT = HAPPY_VICTOR.get_rect(center=(WIDTH/2, 525))
            screen.blit(HAPPY_VICTOR, HAPPY_RECT)
    

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: 
                    inventory_open = False 

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
            button.change_color(MENU_MOUSE_POS)
            button.update(screen)

        
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(BACK_TO, BACK_RECT)

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    print("Play button pressed!")  # Debug
                    play(game)
                if INFO_BUTTON.check_for_input(MENU_MOUSE_POS):
                    game_info(game)
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pg.quit()
                    

        pg.display.update()


main_menu(game)

