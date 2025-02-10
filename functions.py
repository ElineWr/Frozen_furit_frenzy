
from bilder import * 
from constants import * 

backgrounds = [house, coast, camp, cave]  # Liste over bakgrunnsbilder
current_background_index = 0  # Start med house
background = [backgrounds[current_background_index]]

def change_background(player):
    global current_background_index  

    # Bytt bakgrunn basert på spillerens posisjon
    # Fra house til coast
    if current_background_index == 0 and player.x >= WIDTH - player.width:  
        current_background_index = 1
        player.x = 10

    # Fra coast tilbake til house 
    elif current_background_index == 1 and player.x <= 0:  # Fra coast tilbake til house
        current_background_index = 0
        player.x = WIDTH - player.width - 10
       
    # Fra coast til camp
    elif current_background_index == 1 and player.y <= 0: 
        current_background_index = 2
        player.y = HEIGHT - player.height - 10
       
    # Fra camp til cave
    elif current_background_index == 2 and player.y <= 0: 
        current_background_index = 3
        player.y = HEIGHT - player.height - 10
       
    # Fra cave tilbake til camp
    elif current_background_index == 3 and player.y >= HEIGHT - player.height:
        current_background_index = 2
        player.y = 10
    
    # Fra camp til coast
    elif current_background_index == 2 and player.y >= HEIGHT - player.height:
        current_background_index = 1
        player.y = 10

         
    


    background[0] = backgrounds[current_background_index]  # Oppdater bakgrunn

