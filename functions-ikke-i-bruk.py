
from bilder import * 
from constants import * 



backgrounds = [house, coast, camp, cave]  # Liste over bakgrunnsbilder
current_background_index = 0
background = [backgrounds[current_background_index]]

def change_background(player):

    global current_background_index  

    print(f"Player Position: ({player.x}, {player.y})")  # Debug print for player position
    # Bytt bakgrunn basert på spillerens posisjon
    # From house to coast

    if current_background_index == 0 and player.x >= WIDTH - player.width:  
        current_background_index = 1

        player.x = 10
        print("Background changed to coast")

    # From coast back to house
    elif current_background_index == 1 and player.x <= 0:  
        current_background_index = 0

        player.x = WIDTH - 10 - player.width
     
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
        
    #     player.x = WIDTH - player.width - 10
    #     print("Background changed to house")
    
    # # From coast to camp
    # elif current_background_index == 1 and player.y <= 0: 
    #     current_background_index = 2
    #     player.y = HEIGHT - player.height - 10
    #     print("Background changed to camp")
    
    # # From camp to cave
    # elif current_background_index == 2 and player.y <= 0: 
    #     current_background_index = 3
    #     player.y = HEIGHT - player.height - 10
    #     print("Background changed to cave")
    
    # # From cave back to camp
    # elif current_background_index == 3 and player.y >= HEIGHT - player.height:
    #     current_background_index = 2
    #     player.y = 10
    #     print("Background changed to camp")
    
    # # From camp to coast
    # elif current_background_index == 2 and player.y >= HEIGHT - player.height:
    #     current_background_index = 1
    #     player.y = 10
    #     print("Background changed to coast")
    
    # Update the background
    background[0] = backgrounds[current_background_index]  # Update background

