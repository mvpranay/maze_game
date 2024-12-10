import pygame
from main_menu import main_menu
from end_screen import success, death
from player import Player
from game_mechanics import Game
from constants import *
from time import sleep
import sys

pygame.init()

if len(sys.argv) > 1:
    BG_MUSIC = pygame.mixer.Sound(sys.argv[1])

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rabbit Puzzle")
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
        if not pygame.mixer.get_busy():
            BG_MUSIC.play()
        level_clicked = main_menu(screen)
        
        # game
        if not pygame.mixer.get_busy():
            BG_MUSIC.play()
        game = Game(level_clicked, N_CELLS)
        result = game.run(screen) 
        score = game.calculate_score()       
        # end screen
        if result == "success":
            CONTINUE = success(screen, score)
            pygame.mixer.stop()
        elif result == "starved":
            if not pygame.mixer.get_busy():
                BG_MUSIC.play()
            CONTINUE = death(screen, "energy", score)
        elif result == "time_out":
            if not pygame.mixer.get_busy():
                BG_MUSIC.play()
            CONTINUE = death(screen, "time_out", score)

