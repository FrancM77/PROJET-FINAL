import pygame
from pygame.locals import *

pygame.init()

def menu_jeu():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Menu")

    # Loading the background image
    background_screen = pygame.image.load('background.jpeg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Checkbox parameters
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    checkbox_x, checkbox_y = 500, 500
    checkbox_width, checkbox_height = 200, 200
    checkbox_color = BLACK
    checked = False
    
    
    running = True
    while running:
        screen.blit(background_screen, (0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if checkbox_x <= mouse_pos[0] <= checkbox_x + checkbox_width and checkbox_y <= mouse_pos[1] <= checkbox_y + checkbox_height:
                    checked = not checked 

        # Draw the checkbox
        pygame.draw.rect(screen, checkbox_color, (checkbox_x, checkbox_y, checkbox_width, checkbox_height))
        if checked:
            pygame.draw.line(screen, WHITE, (checkbox_x, checkbox_y), (checkbox_x + checkbox_width, checkbox_y + checkbox_height), 3)
            pygame.draw.line(screen, WHITE, (checkbox_x, checkbox_y + checkbox_height), (checkbox_x + checkbox_width, checkbox_y), 3)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
            

    
menu_jeu()