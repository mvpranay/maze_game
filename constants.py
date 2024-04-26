import pygame
WIDTH = 900
HEIGHT = 900
N_CELLS = 20
FPS = 80

BLACK = (0, 0, 0)

MUD_COLOR = (125, 84, 9)
WALL_THICKNESS = 20

PLAYER_VIEW_CELLS = 9
PLAYER_VIEW_SIZE = WIDTH // PLAYER_VIEW_CELLS
PLAYER_SIZE = PLAYER_VIEW_SIZE - WALL_THICKNESS
HALF = (PLAYER_VIEW_CELLS - 1) // 2
BG_SIZE = (N_CELLS + 2 * HALF) * PLAYER_SIZE

RIGHT_IMGS = {}

for i in range(8):
    img = pygame.image.load(f'imgs/{str(i)}.png')
    img = pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
    RIGHT_IMGS[i] = img

LEFT_IMGS = {}
for i in range(8):
    img = RIGHT_IMGS[i]
    img = pygame.transform.flip(img, flip_x=True, flip_y=False)
    LEFT_IMGS[i] = img

UP_IMGS = {}
for i in range(5):
    UP_IMGS[i] = RIGHT_IMGS[i]

DOWN_IMGS = {}
for i in range(4, 8):
    DOWN_IMGS[i] = RIGHT_IMGS[i]

IMG_TICK_DICT_RIGHT = {
    1:1,
    2:1,
    3:2,
    4:3,
    5:2,
    6:1,
    7:1
}

IMG_TICK_DICT_LEFT = {
    1:1,
    2:1,
    3:2,
    4:3,
    5:2,
    6:1,
    7:1
}

IMG_TICK_DICT_UP = {
    1:2,
    2:4,
    3:4,
    4:4
}

IMG_TICK_DICT_DOWN = {
    4:2,
    5:4,
    6:4,
    7:4
}

MAX_MOVE_TICKS_RIGHT = sum(IMG_TICK_DICT_RIGHT.values())
MAX_MOVE_TICKS_LEFT = sum(IMG_TICK_DICT_LEFT.values())
MAX_MOVE_TICKS_UP = sum(IMG_TICK_DICT_UP.values())
MAX_MOVE_TICKS_DOWN = sum(IMG_TICK_DICT_DOWN.values())