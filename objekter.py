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
        self.width = 82.66  
        self.height = 83.66 
        self.is_collected = False  

    def get_image(self, frame, width_food, height_food, scale, color):
        image = pg.Surface((width_food, height_food), pg.SRCALPHA).convert_alpha()
        image.blit(self.image, (0, 0), (frame * width_food, 0, width_food, height_food))
        image = pg.transform.scale(image, (int(width_food * scale), int(height_food * scale)))
        image.set_colorkey(color)
        return image


    def movement(self):
         pass
    

        
    def detect_collision_with_food(self, player, game, food_items):
        player_rect = pg.Rect(player.x, player.y, player.width, player.height)

        for food in food_items:
            #print(food)
            food_rect = pg.Rect(food.x, food.y, food.width, food.height)

            #keys_pressed = pg.key.get_pressed()
            #if food.background == 0 and self.is_collected:
                   # if player.carryingFood:
                    #    player.carryingFood.is_collected = False  # Slipp bæret  
                     #   player.carryingFood = None  # Fjern referansen til bæret

                        #eturn False

            if food.background == game.current_background_index:
                
                if player_rect.colliderect(food_rect):
                    #print(f"Spilleren har samlet {food}!") #.image
                    food.is_collected = True  # Marker bæret som samlet  
                    player.carryingFood = food  # Spilleren bærer dette bæret #food 
                    #food.x = player.x + 10  # Plasser bæret nær spilleren  
                    #food.y = player.y + 10  
                    return True  # Kollisjon oppstod med bæret
                
                #if player.carryingFood == food:
                    #player.carryingFood.x = self.x + 5  # Oppdater x-posisjon  
                    #player.carryingFood.y = self.y + 5  # Oppdater y-posisjon

            
                

        return False  # Ingen kollisjon med noen bær
        

all_ber = [
    Food(x = 300, y = 300, image = blaaber, background = 1),
    Food(x = 0, y = 0, image = bjorneber, background = 1),
    Food(x = 50, y = 150, image = appelsin, background = 1),
    Food(x = 950, y = 330, image = blaaber, background = 2),
    Food(x = 0, y = 0, image = bringeber, background = 2),
    Food(x = 0, y = 0, image = appelsin, background = 2),
    Food(x = 200, y = 100, image = bjorneber, background = 3),
    Food(x = 0, y = 0, image = bringeber, background = 3),
    ]

            

ber = pg.sprite.Group()
ber.add(all_ber)

        


    
#frame_0 = ber.get_image(frame = 0, width_food = 82.66, height_food=83.66, scale=1, color=BLACK)




class Isbjorn(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)



