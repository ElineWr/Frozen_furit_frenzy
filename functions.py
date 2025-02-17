
from bilder import * 
from constants import * 



backgrounds = [house, coast, camp, cave]  # Liste over bakgrunnsbilder
current_background_index = 0
background = [backgrounds[current_background_index]]

def change_background(player):
    global current_background_index
    # Fra house til coast
    if current_background_index == 0 and player.x >= WIDTH - player.width:  
        current_background_index = 1
        print(current_background_index)
        player.x = 10

    # Fra coast tilbake til house 
    elif current_background_index == 1 and player.x <= 0:  # Fra coast tilbake til house
        current_background_index = 0
        player.x = WIDTH - 10 - player.width
        print(current_background_index)
       
    # Fra coast til camp
    elif current_background_index == 1 and player.y <= 0: 
        current_background_index = 2
        player.y = HEIGHT - player.height - 10
        print(current_background_index)
    # Fra camp til cave
    elif current_background_index == 2 and player.y <= 0: 
        current_background_index = 3
        player.y = HEIGHT - player.height - 10
        print(current_background_index)
       
    # Fra cave tilbake til camp
    elif current_background_index == 3 and player.y >= HEIGHT - player.height:
        current_background_index = 2
        player.y = 10
        print(current_background_index)
    # Fra camp til coast
    elif current_background_index == 2 and player.y >= HEIGHT - player.height:
        current_background_index = 1
        player.y = 10
        print(current_background_index)
    

    background[0] = backgrounds[current_background_index]  # Oppdater bakgrunn

    
