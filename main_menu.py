import pygame
from constants import *

def main_menu(screen):
    run = True
    level_selected = None
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

        start_text = level_font.render("Press Enter to Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 210))
        screen.blit(start_text, start_rect)
        
        if level_selected == "Easy":
            pygame.draw.rect(screen, (0, 255, 0), easy_rect, 1)
        elif level_selected == "Medium":
            pygame.draw.rect(screen, (255, 165, 0), medium_rect, 1)
        elif level_selected == "Hard":
            pygame.draw.rect(screen, (255, 0, 0), hard_rect, 1)

        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if easy_rect.collidepoint(mouse_pos):
                    level_selected = "Easy"
                elif medium_rect.collidepoint(mouse_pos):
                    level_selected = "Medium"
                elif hard_rect.collidepoint(mouse_pos):
                    level_selected = "Hard"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and level_selected is not None:
                    run = False
    
    return level_selected