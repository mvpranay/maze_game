import pygame
from constants import *

def success(screen):
    
    font = pygame.font.Font(None, 80)
    continue_font = pygame.font.Font(None, 40)

    run = True
    while run:
        screen.fill(BLACK)

        text = font.render("Congrats you won!!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        continue_text = continue_font.render("Continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 100))

        end_text = continue_font.render("Exit", True, (255, 255, 255))
        end_rect = end_text.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 + 100))
        
        mouse_pos = pygame.mouse.get_pos()
        if continue_rect.collidepoint(mouse_pos):
            continue_text = continue_font.render("Continue", True, (0, 255, 0))  # Green color
        elif end_rect.collidepoint(mouse_pos):
            end_text = continue_font.render("Exit", True, (255, 0, 0)) # Red color
        
        screen.blit(continue_text, continue_rect)
        screen.blit(end_text, end_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_rect.collidepoint(mouse_pos):
                    return True
                elif end_rect.collidepoint(mouse_pos):
                    return False
                
def starved(screen):
    font = pygame.font.Font(None, 80)
    continue_font = pygame.font.Font(None, 40)
    while True:
        screen.fill(BLACK)

        text1 = font.render("You ran out of energy : (", True, (255, 255, 255))
        text1_rect = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text1, text1_rect)

        continue_text = continue_font.render("Continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 100))

        exit_text = continue_font.render("Exit", True, (255, 255, 255))
        exit_rect = exit_text.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 + 100))

        mouse_pos = pygame.mouse.get_pos()
        if continue_rect.collidepoint(mouse_pos):
            continue_text = continue_font.render("Continue", True, (0, 255, 0))  # Green color
        elif exit_rect.collidepoint(mouse_pos):
            exit_text = continue_font.render("Exit", True, (255, 0, 0)) # Red color
                
        screen.blit(continue_text, continue_rect)
        screen.blit(exit_text, exit_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_rect.collidepoint(mouse_pos):
                    return True
                elif exit_rect.collidepoint(mouse_pos):
                    return False
                
def time_out(screen):
    font = pygame.font.Font(None, 80)
    continue_font = pygame.font.Font(None, 40)
    while True:
        screen.fill(BLACK)

        text1 = font.render("You ran out of time : (", True, (255, 255, 255))
        text1_rect = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text1, text1_rect)

        continue_text = continue_font.render("Continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 100))

        exit_text = continue_font.render("Exit", True, (255, 255, 255))
        exit_rect = exit_text.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 + 100))

        mouse_pos = pygame.mouse.get_pos()
        if continue_rect.collidepoint(mouse_pos):
            continue_text = continue_font.render("Continue", True, (0, 255, 0))  # Green color
        elif exit_rect.collidepoint(mouse_pos):
            exit_text = continue_font.render("Exit", True, (255, 0, 0)) # Red color
                
        screen.blit(continue_text, continue_rect)
        screen.blit(exit_text, exit_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if continue_rect.collidepoint(mouse_pos):
                    return True
                elif exit_rect.collidepoint(mouse_pos):
                    return False