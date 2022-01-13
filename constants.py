import pygame as pg

AUTHOR = "kadraman's"
TITLE = "Galaxy Blast"
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 30
ENEMY_MOVE_DOWN = 16
SPRITE_SHEET = './assets/images/spritesheet.png'
DEFAULT_FONT = './assets/fonts/BarcadeBrawlRegular.ttf'
DEFAULT_FONT_SIZE = 18
TITLE_FONT = "./assets/fonts/OASIS.TTF"
TITLE_FONT_SIZE = 48
DEFAULT_BACKGROUND = './assets/images/stars.png'
PLAY_SOUNDS = True

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 0)
GREEN = (0, 0, 0)
BLUE = (0, 0, 0)

TXT_CREDITS = 'This game was written by kadraman'

# user defined events
ADD_MINION_ENEMY = pg.USEREVENT + 1  # 25
ADD_MASTER_ENEMY = pg.USEREVENT + 2  # 26
DIVE_ENEMY = pg.USEREVENT + 3  # 27
LEAVE_ENEMY = pg.USEREVENT + 4  # 28
ENEMY_FIRES = pg.USEREVENT + 5  # 29

MINION_ENEMY_WIDTH = 25
MINION_ENEMY_HEIGHT = 25
MASTER_ENEMY_WIDTH = 30
MASTER_ENEMY_HEIGHT = 28
BOSS_ENEMY_WIDTH = 25
BOSS_ENEMY_HEIGHT = 25

'''
locations of sprites in sprite sheet
'''
# player
SS_PLAYER_PIXEL_SIZE = 32
SS_PLAYER_X = 224
SS_PLAYER_Y = 832
SS_PLAYER_WIDTH = 99
SS_PLAYER_HEIGHT = 75
SS_PLAYER_IMAGES = 1
# enemies
SS_ENEMY1_PIXEL_SIZE = 20
SS_ENEMY1_X = 425
SS_ENEMY1_Y = 552
SS_ENEMY1_WIDTH = 93
SS_ENEMY1_HEIGHT = 84
SS_ENEMY1_IMAGES = 1
# missile
SS_MISSILE_X = 841
SS_MISSILE_Y = 647
SS_MISSILE_WIDTH = 13
SS_MISSILE_HEIGHT = 37
SS_MISSILE_IMAGES = 1
# explosion
SS_EXPLOSION_X = 80
SS_EXPLOSION_Y = 0
SS_EXPLOSION_WIDTH = 40
SS_EXPLOSION_HEIGHT = 40
SS_EXPLOSION_IMAGES = 3
# player lives
SS_PLAYER_LIVES_X = 775
SS_PLAYER_LIVES_Y = 301
SS_PLAYER_LIVES_WIDTH = 33
SS_PLAYER_LIVES_HEIGHT = 26
