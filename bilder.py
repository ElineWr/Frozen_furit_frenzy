import pygame as pg
from constants import SIZE
# bakgrunnsbilder
house = pg.image.load("assets/house.png").convert_alpha()
camp = pg.image.load("assets/camp.webp").convert_alpha()
cave = pg.image.load("assets/cave.webp").convert_alpha()
coast = pg.image.load("assets/coast.webp").convert_alpha()

# skalering av bakgrunnsbildene
house = pg.transform.scale(house, SIZE)
camp = pg.transform.scale(camp, SIZE)
cave = pg.transform.scale(cave, SIZE)
coast = pg.transform.scale(coast, SIZE)

victor = pg.image.load("assets/victor-removebg-preview.png").convert_alpha()
victor = pg.transform.scale(victor, (629, 75))

victor_info = pg.image.load("assets/victor_info.png").convert_alpha()

victor_opp = pg.image.load("assets/victor_opp.jpg").convert_alpha()
victor_opp = pg.transform.scale(victor_opp, (629, 75))

victor_left = pg.transform.flip(victor, True, False)
#victor_left = pg.transform.scale(victor_left, (629, 75))

blaaber = pg.image.load("assets/bluberry_hover.png").convert_alpha()
blaaber = pg.transform.scale(blaaber, (330.66, 83.66))
bjorneber = pg.image.load("assets/blackberry_hover.png").convert_alpha()
appelsin = pg.image.load("assets/orange_hover.png").convert_alpha()
bringeber = pg.image.load("assets/raspberry_hover.png").convert_alpha()

tekst_bakgrunn = pg.image.load("assets/txt_background.png").convert_alpha()
info_rect = pg.image.load("assets/Options Rect.png").convert_alpha()
play_rect = pg.image.load("assets/Play Rect.png").convert_alpha()
quit_rect = pg.image.load("assets/Quit Rect.png").convert_alpha()
test = pg.image.load("assets/test.webp").convert_alpha()
pause_menu = pg.image.load("assets/Pause Rect.png").convert_alpha()



