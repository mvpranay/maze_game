import pygame
WIDTH = 900
HEIGHT = 900
N_CELLS = 20
FPS = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MUD_COLOR = (109, 58, 31)#(139, 69, 19)
STONE_COLOR = (158, 158, 158)
WALL_THICKNESS = 20

PLAYER_VIEW_CELLS = 9
PLAYER_VIEW_SIZE = WIDTH // PLAYER_VIEW_CELLS
PLAYER_SIZE = PLAYER_VIEW_SIZE - WALL_THICKNESS
HALF = (PLAYER_VIEW_CELLS - 1) // 2
BG_SIZE = (N_CELLS + 2 * HALF) * PLAYER_SIZE

OPENING_IMAGE = pygame.image.load('imgs/opening_screen.png')
OPENING_IMAGE = pygame.transform.scale(OPENING_IMAGE, (WIDTH, HEIGHT))

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

# BG_IMAGE = pygame.image.load('imgs/possible_background.jpg')
BG_IMAGE = pygame.image.load('imgs/BG_IG.png')
BG_IMAGE = pygame.transform.scale(BG_IMAGE, ((N_CELLS + 2*HALF) * PLAYER_VIEW_SIZE,) * 2)
CELL_IMAGE = pygame.image.load('imgs/tile.png')
CELL_IMAGE = pygame.transform.scale(CELL_IMAGE, (PLAYER_VIEW_SIZE, PLAYER_VIEW_SIZE))

CARROT = pygame.image.load('imgs/carrot.png')
CARROT = pygame.transform.scale(CARROT, (PLAYER_SIZE, PLAYER_SIZE))
GOLDEN_CARROT = pygame.image.load('imgs/golden_carrot.png')
GOLDEN_CARROT = pygame.transform.scale(GOLDEN_CARROT, (PLAYER_SIZE, PLAYER_SIZE))

FOOD_SIZE = 40
FOOD = pygame.image.load('imgs/food.png')
FOOD = pygame.transform.scale(FOOD, (FOOD_SIZE, FOOD_SIZE))

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
    2:2,
    3:3,
    4:4
}

IMG_TICK_DICT_DOWN = {
    4:2,
    5:2,
    6:3,
    7:4
}

MAX_MOVE_TICKS_RIGHT = sum(IMG_TICK_DICT_RIGHT.values())
MAX_MOVE_TICKS_LEFT = sum(IMG_TICK_DICT_LEFT.values())
MAX_MOVE_TICKS_UP = sum(IMG_TICK_DICT_UP.values())
MAX_MOVE_TICKS_DOWN = sum(IMG_TICK_DICT_DOWN.values())

MAX_TIME_ALLOWED = {"Easy": 60, "Medium": 100, "Hard": 150}

N_CARROTS = {"Easy": 10, "Medium": 15, "Hard": 20}
MAX_ENERGY = 10 
MAX_ENERGY_TICKS = 8

MAX_STARVE_TICKS = 10