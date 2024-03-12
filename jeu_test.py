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
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from menu_staryinsh import menu
                menu()
                running=False
                pygame.quit()
            
    
menu_jeu()