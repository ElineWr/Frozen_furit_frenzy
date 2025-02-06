
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

    # Fra coast tilbake til house 
    elif current_background_index == 1 and player.x <= 0:  # Fra coast tilbake til house
        current_background_index = 0
       
    # Fra coast til camp
    elif current_background_index == 1 and player.y <= 0: 
        current_background_index = 2
       
    # Fra camp til cave
    elif current_background_index == 2 and player.y <= 0: 
        current_background_index = 3
       
    # Fra cave tilbake til camp
    elif current_background_index == 3 and player.y >= HEIGHT - player.height:
        current_background_index = 2
    
    # Fra camp til coast
    elif current_background_index == 2 and player.y >= HEIGHT - player.height:
        current_background_index = 1

         
    


    background[0] = backgrounds[current_background_index]  # Oppdater bakgrunn

