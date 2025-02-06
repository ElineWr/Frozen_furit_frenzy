
from objekter import Object
from constants import PLAYER_SPEED, WIDTH, HEIGHT
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from bilder import *

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

    def beat(self, x, y, carryingFood):
        pass

    def move(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT] and self.x > 0:
            self.x -= PLAYER_SPEED
            self.image = victor
        if keys_pressed[K_RIGHT] and self.x < WIDTH:
            self.x += PLAYER_SPEED
        if keys_pressed[K_UP] and self.y > 0:
            self.y -= PLAYER_SPEED
            self.image = victor
        if keys_pressed[K_DOWN] and self.y < HEIGHT:
            self.y += PLAYER_SPEED
            self.image = victor

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

