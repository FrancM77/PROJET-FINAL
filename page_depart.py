import pygame
from pygame.locals import *

pygame.init()

def start():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Start")

    # Loading the background image
    background_screen = pygame.image.load('start.jpg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    running=True 
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            keys = pygame.key.get_pressed()
            if any(keys):
                from menu_staryinsh import menu
                menu()
        screen.blit(background_screen, (0, 0))
        pygame.display.flip()

    pygame.quit()
                
start()