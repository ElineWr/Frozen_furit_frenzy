
from objekter import Object, Food
from constants import PLAYER_SPEED, WIDTH, HEIGHT, BLACK
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *
from game import Game
from objekter import Food

#from main import *

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width_sprite, height_sprite, scale, color):
        image = pg.Surface((width_sprite, height_sprite)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width_sprite), 0, width_sprite, height_sprite))
        image = pg.transform.scale(image, (width_sprite * scale, height_sprite * scale))
        image.set_colorkey(color)

        return image



class Player(Object):

    def __init__(self, x, y, dy, dx, image, money, carryingFood):
        super().__init__(x, y, image)
        self.dy = dy
        self.dx = dx
        self.money = money
        self.carryingFood = None
        self.handling = 1  # Initial handling (state)
        self.frame = 0
        self.sheet_type = victor  # Initial sprite sheet
        self.last_update_time = pg.time.get_ticks()  # Time of last frame update
        self.animation_cooldown = 100 
        self.flipped = False
        self.height = self.image.get_height()
        self.width = 40 # bredden brukt til sprite
        self.collected_foods = []
        self.food_count = {  # Dictionary for å holde styr på antall  
            "blaaber": 0,
            "bjorneber": 0,
            "bringebær": 0,
            "appelsin": 0  
        }

    def beat(self, x, y, carryingFood):
            pass

    def collect_food(self, food):
        self.collected_foods.append(food)  # Legg til bæret i inventaret

        # Oppdater antall i food_count basert på typen av bær  
        if food.image == blaaber:
            self.food_count["blaaber"] += 1  
        elif food.image == bjorneber:
            self.food_count["bjorneber"] += 1  
        elif food.image == bringeber:
            self.food_count["bringebær"] += 1  
        elif food.image == appelsin:
            self.food_count["appelsin"] += 1

    
    def move(self, squares, game):
        keys_pressed = pg.key.get_pressed()

        # Lagre den nåværende posisjonen til spilleren  
        old_x = self.x  
        old_y = self.y

        # Beveg spilleren basert på tastetrykk  
        if keys_pressed[K_LEFT]:
            self.x = max(self.x - PLAYER_SPEED, 0)
            self.flipped = True
            self.handling = 0  # Handling for left
            self.dx = -PLAYER_SPEED
            # Animasjonslogikk kan settes her hvis ønskelig

        elif keys_pressed[K_RIGHT]:
            self.x = min(self.x + PLAYER_SPEED, WIDTH - self.width)
            self.flipped = False
            self.handling = 0  # Handling for right
            self.dx = PLAYER_SPEED
            # Animasjonslogikk kan settes her hvis ønskelig

        if keys_pressed[K_UP]:
            self.y = max(self.y - PLAYER_SPEED, 0)
            self.handling = 1  # Handling for up
            self.sheet_type = victor_opp  # Opp animasjon
            self.dy = -PLAYER_SPEED
        
        elif keys_pressed[K_DOWN]:
            self.y = min(self.y + PLAYER_SPEED, HEIGHT - self.height)
            self.handling = 0  # Handling for down
            self.dy = PLAYER_SPEED
            if self.sheet_type == victor_opp:
                self.sheet_type = victor  # Endre til ned animasjon
        # Sjekk for kollisjon med firkanter  
        for square in squares:
            if square.detect_collision(self, game):
                # Hvis det oppstår en kollisjon, tilbakestill posisjonen  
                self.x = old_x  
                self.y = old_y  
                break  # Ingen grunn til å sjekke flere firkanter  

        # Sjekk for bakgrunnsendring etter kollisjoner er håndtert  
        if self.x >= WIDTH - self.width:  # Høyre kant  
            game.change_background(self)
        elif self.x <= 0:  # Venstre kant  
            game.change_background(self)
        elif self.y <= 0:  # Toppkant  
            game.change_background(self)
        elif self.y >= HEIGHT - self.height:  # Bunnkant  
            game.change_background(self)
            
    
        
        # Frame update based on animation cooldown
        current_time = pg.time.get_ticks()
        if current_time - self.last_update_time >= self.animation_cooldown:
            self.frame += 1
            self.last_update_time = current_time  # Update the last frame update time
            self.dy = -PLAYER_SPEED
            if self.frame >= len(animasjons_liste[self.handling]):  # Loop the frames
                self.frame = 0

        if self.carryingFood:
            self.carryingFood.x = self.x + 5  # Oppdater x-posisjon  
            self.carryingFood.y = self.y + 5  # Oppdater y-posisjon
            
        if keys_pressed[pg.K_d] and self.carryingFood:
            self.carryingFood.is_collected = False  # Slipp bæret  
            self.carryingFood = None  # Fjern referansen til bæret
                
            
    
    def draw(self, screen):
    # Sjekk om handlingen er gyldig
        if 0 <= self.handling < len(animasjons_liste):
        # Sjekk om frame er gyldig
            if len(animasjons_liste[self.handling]) > 0:
                self.frame = self.frame % len(animasjons_liste[self.handling])  # Sørg for at frame er gyldig
                img = animasjons_liste[self.handling][self.frame]
                if self.flipped:
                    img = pg.transform.flip(img, True, False).convert_alpha()
                screen.blit(img, (self.x, self.y))
            else:
                print(f"Ugyldig animasjonsliste for handling {self.handling}")
        else:
            print(f"Ugyldig handling: {self.handling}")

    def colisjon_mat(self, ber):
        if pg.sprite.spritecollide(self, ber, True):
            print("colisjon!")

        
        

# def draw(self, screen):
#     if 0 <= self.handling < len(animasjons_liste):
#         if len(animasjons_liste[self.handling]) > 0:
#             self.frame = self.frame % len(animasjons_liste[self.handling])
#             img = animasjons_liste[self.handling][self.frame]
#             if self.flipped:
#                 img = pg.transform.flip(img, True, False).convert_alpha()
#             screen.blit(img, (self.x, self.y))
#         else:
#             print(f"Ugyldig animasjonsliste for handling {self.handling}")
#     else:
#         print(f"Ugyldig handling: {self.handling}")



player = Player(x = 700, y = 220, dx = 1, dy = 1, image = victor, money = 0, carryingFood = False)  #WIDTH/2+5, 260)


animasjons_liste = []
steps_teller = 0
animasjon_steps = [6, 3]   
sheet_type = victor

sprite_sheet = SpriteSheet(sheet_type)

handling = 1
siste_oppdadering = pg.time.get_ticks()
frame = 0


for animasjons in animasjon_steps: # !
    midlertidig_bilde_liste = [] 
    for _ in range(animasjons):
        midlertidig_bilde_liste.append(sprite_sheet.get_image(steps_teller, 40, 75, 1.5, BLACK))
        steps_teller += 1
    animasjons_liste.append(midlertidig_bilde_liste)


