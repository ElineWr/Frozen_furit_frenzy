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

blaaber = pg.image.load("assets/blueberry.png").convert_alpha()
blaaber = pg.transform.scale(blaaber, (82.66, 83.66))
bjorneber = pg.image.load("assets/blackberry.png").convert_alpha()
bjorneber = pg.transform.scale(bjorneber, (82.66, 83.66))
appelsin = pg.image.load("assets/orange.webp").convert_alpha()
appelsin = pg.transform.scale(appelsin, (82.66, 83.66))
bringeber = pg.image.load("assets/raspberry.png").convert_alpha()
bringeber = pg.transform.scale(bringeber, (82.66, 83.66))


info_rect = pg.image.load("assets/Options Rect.png").convert_alpha()
play_rect = pg.image.load("assets/Play Rect.png").convert_alpha()
quit_rect = pg.image.load("assets/Quit Rect.png").convert_alpha()
pause_menu = pg.image.load("assets/Pause Rect.png").convert_alpha()
menu_bck = pg.image.load("assets/Title Rect.png").convert_alpha()
offwhite_bg = pg.image.load("assets/offwhite_bck.png").convert_alpha()


