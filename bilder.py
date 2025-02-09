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

victor_opp = pg.image.load("assets/victor_opp.jpg").convert_alpha()
victor_opp = pg.transform.scale(victor_opp, (629, 75))

victor_left = pg.transform.flip(victor, True, False)
#victor_left = pg.transform.scale(victor_left, (629, 75))