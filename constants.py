WIDTH = 900
HEIGHT = 900
N_CELLS = 20
FPS = 80

BLACK = (50,) * 3
WHITE = (230,) * 3
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

fill_color = (125, 84, 9)
WALL_THICKNESS = 20

PLAYER_VIEW_CELLS = 9
PLAYER_VIEW_SIZE = WIDTH // PLAYER_VIEW_CELLS
PLAYER_SIZE = PLAYER_VIEW_SIZE - WALL_THICKNESS
HALF = (PLAYER_VIEW_CELLS - 1) // 2
BG_SIZE = (N_CELLS + 2 * HALF) * PLAYER_SIZE

# IMG_TICK_DICT = {
#     1:2,
#     2:2,
#     3:3,
#     4:4,
#     5:3,
#     6:2,
#     7:2
# }

IMG_TICK_DICT = {
    1:1,
    2:1,
    3:2,
    4:3,
    5:2,
    6:1,
    7:1
}

MAX_MOVE_TICKS = sum(IMG_TICK_DICT.values())
