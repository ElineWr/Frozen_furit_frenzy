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
        image = pg.Surface((width_food, height_food)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * width_food), 0, width_food, height_food))
        image = pg.transform.scale(image, (width_food * scale, height_food * scale))
        image.set_colorkey(color)

        return image

    def movement(self):
         pass
    
         
    def draw(self, background):

        if background == 1:
            self.screen.blit(bjorneber, (300, 300))
            self.screen.blit(bringeber, (50, 150))
            self.screen.blit(appelsin, (60, 60))
            #print(f"Food position updated to coast: ({food_x}, {food_y})")
            
            
        elif background == 2:
            self.screen.blit(bjorneber, (950, 330))
            self.screen.blit(blaaber, (20, 20))
            self.screen.blit(bringeber, (40, 40))
            #print(f"Food position updated to coast: ({food_x}, {food_y})")
 
        elif background == 3:

            self.screen.blit(appelsin, (200, 100))
            self.screen.blit(blaaber, (10, 10))
            #print(f"Food position updated to coast: ({food_x}, {food_y})")

        

        #screen.blit(blaaber, (self.x, self.y)) 
    
"""   
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
"""
        


    
#frame_0 = ber.get_image(frame = 0, width_food = 82.66, height_food=83.66, scale=1, color=BLACK)




class Isbjorn(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)



