
from objekter import Object
from constants import PLAYER_SPEED, WIDTH, HEIGHT, BLACK
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *
from functions import get_current_grid, current_background_index
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

    def __init__(self, x, y, dy, image, money, carryingFood):
        super().__init__(x, y, image)
        self.dy = dy
        self.money = money
        self.carryingFood = carryingFood
        self.handling = 1  # Initial handling (state)
        self.frame = 0
        self.sheet_type = victor  # Initial sprite sheet
        self.last_update_time = pg.time.get_ticks()  # Time of last frame update
        self.animation_cooldown = 100 
        self.flipped = False
        self.height = self.image.get_height()
        self.width = 40

        def beat(self, x, y, carryingFood):
            pass


    
    def move(self):
        keys_pressed = pg.key.get_pressed()
        original_x = self.x
        original_y = self.y

        
        if keys_pressed[K_LEFT]:
            self.x = max(self.x - PLAYER_SPEED, 0)  # Hindrer at x blir mindre enn self.width  
            new_x = self.x - PLAYER_SPEED
            # Sjekk om den nye posisjonen er blokkert på x-aksen
            if not get_current_grid(current_background_index).is_blocked(new_x, self.y):
                self.x = new_x  # Oppdater x hvis ikke blokkert
        if keys_pressed[K_RIGHT]:
            self.x = min(self.x + PLAYER_SPEED, WIDTH - self.width)  # Hindrer at x går over WIDTH - self.width
            new_x = self.x + PLAYER_SPEED
            # Sjekk om den nye posisjonen er blokkert på x-aksen
            if not get_current_grid(current_background_index).is_blocked(new_x, self.y):
                self.x = new_x  # Oppdater x hvis ikke blokkert

            
        if keys_pressed[K_UP]:
            self.y = max(self.y - PLAYER_SPEED, 0)  # Hindrer at y blir negativ
            new_y = self.y - PLAYER_SPEED
            # Sjekk om den nye posisjonen er blokkert på y-aksen
            if not get_current_grid(current_background_index).is_blocked(self.x, new_y):
                self.y = new_y  # Oppdater y hvis ikke blokkert

        if keys_pressed[K_DOWN]:
            self.y = min(self.y + PLAYER_SPEED, HEIGHT - self.height)  # Hindrer at y går over HEIGHT - self.height
            new_y = self.y + PLAYER_SPEED
            # Sjekk om den nye posisjonen er blokkert på y-aksen
            if not get_current_grid(current_background_index).is_blocked(self.x, new_y):
                self.y = new_y  # Oppdater y hvis ikke blokkert


        # Handling the LEFT 
        if keys_pressed[K_LEFT] and self.x >= 0:
            self.x -= PLAYER_SPEED
            self.handling = 0
            #self.frame = 0
            #victor_left = pg.transform.flip(victor, True, False)
            #self.sheet_type = victor_left
            self.flipped = True

        # Handling the RIGHT 
        if keys_pressed[K_RIGHT] and self.x <= WIDTH:
            self.x += PLAYER_SPEED
            self.handling = 0  # Set handling to the right animation
            #self.frame = 0  # Reset to the first frame of the right animation
            #self.sheet_type = victor  # Change to the sprite sheet for right
            self.flipped = False

        # Handling UP 
        if keys_pressed[K_UP] and self.y >= 0: #and self.handling < len(animasjons_liste) - 1:
            self.y -= PLAYER_SPEED
            self.handling = 1  # Moving up, set to up animation
            #self.frame = 0  # Reset to first frame of the up animation
            self.sheet_type = victor_opp  # Change to the sprite sheet for up

        # Handling DOWN 
        if keys_pressed[K_DOWN] and self.y < HEIGHT and self.handling >= 0:
            self.y += PLAYER_SPEED
            self.handling = 0 
            #self.frame = 0 
            if self.sheet_type == victor_opp:
                self.sheet_type = victor  

        # Frame update based on animation cooldown
        current_time = pg.time.get_ticks()
        if current_time - self.last_update_time >= self.animation_cooldown:
            self.frame += 1
            self.last_update_time = current_time  # Update the last frame update time
            if self.frame >= len(animasjons_liste[self.handling]):  # Loop the frames
                self.frame = 0

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


