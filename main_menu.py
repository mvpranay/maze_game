import pygame
from constants import *

def main_menu(screen):
    run = True
    while run:
        screen.fill(BLACK)
        title_font = pygame.font.Font(None, 80)
        title_text = title_font.render("Rabbit Puzzle", True, (255, 255, 255))  
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)

        level_font = pygame.font.Font(None, 60)  

        easy_text = level_font.render("Easy", True, (0, 255, 0))
        easy_rect = easy_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        medium_text = level_font.render("Medium", True, (255, 165, 0))
        medium_rect = medium_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))

        hard_text = level_font.render("Hard", True, (255, 0, 0))
        hard_rect = hard_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
        
        mouse_pos = pygame.mouse.get_pos()
        if easy_rect.collidepoint(mouse_pos):
            easy_text = level_font.render("Easy", True, (0, 128, 0))

        if medium_rect.collidepoint(mouse_pos):
            medium_text = level_font.render("Medium", True, (128, 82, 0))

        if hard_rect.collidepoint(mouse_pos):
            hard_text = level_font.render("Hard", True, (128, 0, 0))

        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if easy_rect.collidepoint(mouse_pos):
                    return "Easy"
                elif medium_rect.collidepoint(mouse_pos):
                    return "Medium"
                elif hard_rect.collidepoint(mouse_pos):
                    return "Hard"
    
    return None