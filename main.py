import pygame
from main_menu import main_menu
from end_screen import success, starved, time_out
from player import Player
from game import Game
from constants import *
from time import sleep

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

def checkValidMove(player: Player, direction, cells):
    current_cell = cells[player.row][player.col]
    wall_exists = bool(eval(f"current_cell.{direction}"))
    if wall_exists:
        return False
    return True

def opening_screen(screen):
    screen.fill(BLACK)
    rect = (0, 0, WIDTH, HEIGHT)
    screen.blit(OPENING_IMAGE, rect)
    pygame.display.update()
    sleep(3)
    return

if __name__ == "__main__":
    opening_screen(screen)

    CONTINUE = True
    while CONTINUE:
        # main menu
        level_clicked = main_menu(screen)

        # game
        game = Game(level_clicked, N_CELLS)
        result = game.run(screen)

        # end screen
        if result == "success":
            CONTINUE = success(screen)
        elif result == "starved":
            CONTINUE = starved(screen)
        elif result == "time_out":
            CONTINUE = time_out(screen)

