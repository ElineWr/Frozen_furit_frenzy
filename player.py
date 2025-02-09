
from objekter import Object
from constants import PLAYER_SPEED, WIDTH, HEIGHT, BLACK
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *
from main import *

animasjons_liste = []
steps_teller = 0
animasjon_steps = [6, 3]   # !
sheet_type = victor



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
        self.animation_cooldown = 300 

    def move(self):
        keys_pressed = pg.key.get_pressed()

        # Handling the LEFT 
        if keys_pressed[K_LEFT] and self.x > 0:
            self.x -= PLAYER_SPEED
            self.handling = 0
            #self.frame = 0
            self.sheet_type = victor_left

        # Handling the RIGHT 
        if keys_pressed[K_RIGHT] and self.x < WIDTH:
            self.x += PLAYER_SPEED
            self.handling = 0  # Set handling to the right animation
            #self.frame = 0  # Reset to the first frame of the right animation
            self.sheet_type = victor  # Change to the sprite sheet for right

        # Handling UP 
        if keys_pressed[K_UP] and self.y > 0: #and self.handling < len(animasjons_liste) - 1:
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
                screen.blit(animasjons_liste[self.handling][self.frame], (self.x, self.y))
            else:
                print(f"Ugyldig animasjonsliste for handling {self.handling}")
        else:
            print(f"Ugyldig handling: {self.handling}")



sprite_sheet = SpriteSheet(sheet_type)


for animasjons in animasjon_steps: # !
    midlertidig_bilde_liste = [] 
    for _ in range(animasjons):
        midlertidig_bilde_liste.append(sprite_sheet.get_image(steps_teller, 40, 75, 1.5, BLACK))
        steps_teller += 1
    animasjons_liste.append(midlertidig_bilde_liste)


