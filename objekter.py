# from functions import *
from player import *
from bilder import *
from constants import *
from game import Game


food_animasjonsliste = []
food_animasjons_steps = 4
food_frame = 0




class Object:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image



class Food(pg.sprite.Sprite):

    def __init__(self, x, y, image, background): 
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.rect = pg.Rect(self.x, self.y, 82.66, 83.66)
        self.background = background 

    def get_image(self, frame, width_food, height_food, scale, color):
        image = pg.Surface((width_food, height_food), pg.SRCALPHA).convert_alpha()
        image.blit(self.image, (0, 0), (frame * width_food, 0, width_food, height_food))
        image = pg.transform.scale(image, (int(width_food * scale), int(height_food * scale)))
        image.set_colorkey(color)
        return image


    def movement(self):
         pass
    

        

        #screen.blit(blaaber, (self.x, self.y)) 
    # def draw(self, screen, player):
    #     # plasering
    #     if game.current_background_index == 0:
    #         pass
    #     elif game.cu == coast:
    #         pass
    #     elif change_background(player) == camp:
    #         pass
    #     elif change_background(player) == cave:
    #         pass


all_ber = [
    Food(x = 300, y = 300, image = blaaber, background = 1),
    Food(x = 0, y = 0, image = bjorneber, background = 1),
    Food(x = 50, y = 150, image = appelsin, background = 1),
    Food(x = 950, y = 330, image = blaaber, background = 2),
    Food(x = 0, y = 0, image = bringeber, background = 2),
    Food(x = 0, y = 0, image = appelsin, background = 2),
    Food(x = 200, y = 100, image = bjorneber, background = 3),
    Food(x = 0, y = 0, image = bringeber, background = 3)]

            

ber = pg.sprite.Group()
ber.add(all_ber)

        


    
#frame_0 = ber.get_image(frame = 0, width_food = 82.66, height_food=83.66, scale=1, color=BLACK)




class Isbjorn(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)



