import pygame as pg
from enrty_db import *
vec = pg.math.Vector2


# GAME settings
WIDTH = 1080
HEIGHT = 720
TITLE = "Rush And Shoot"
CELL = 30
WALL_IMG = 'block_06.png'
MAP_LVL = ['map.txt', 'map2.txt']
FONT = 'data/font.ttf'
# UNITS settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ID = get_selected_user()
PLAYER_IMG = get_user_model(PLAYER_ID)
ENEMY_IMG = ['enemy1.png', 'enemy2.png', 'enemy3.png']
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 300
BULLET_DAMAGE = 10









