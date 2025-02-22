# from functions import *
from player import *
from bilder import *
from constants import *

class Object:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image



class Food(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def get_image(self, frame, width_food, height_food, scale, color):
        image = pg.Surface((width_food, height_food)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * width_food), 0, width_food, height_food))
        #image = pg.transform.scale(image, (width_food * scale, height_food * scale))
        image.set_colorkey(color)

        return image

    def movement(self):
         pass
    
         
    def draw(self, screen, player):

        # plasering
        if change_background(player) == house:
            pass
        elif change_background(player) == coast:
            pass
        elif change_background(player) == camp:
            pass
        elif change_background(player) == cave:
            pass

        #screen.blit(blaaber, (self.x, self.y)) 
        
blaaber_1 = Food(x = 0, y = 0, image = blaaber)
    
frame_0 = blaaber_1.get_image(frame = 0, width_food = 82.66, height_food=83.66, scale=1, color=BLACK)




class Isbjorn(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)



