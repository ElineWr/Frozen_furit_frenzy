import pygame as pg
from constants import SIZE
# bakgrunnsbilder
house = pg.image.load("assets/house.jpg").convert_alpha()
camp = pg.image.load("assets/camp.webp").convert_alpha()
cave = pg.image.load("assets/cave.webp").convert_alpha()
coast = pg.image.load("assets/coast.webp").convert_alpha()

# skalering av bakgrunnsbildene
house = pg.transform.scale(house, SIZE)
camp = pg.transform.scale(camp, SIZE)
cave = pg.transform.scale(cave, SIZE)
coast = pg.transform.scale(coast, SIZE)