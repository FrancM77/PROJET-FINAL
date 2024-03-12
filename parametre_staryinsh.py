import pygame
import pygame_widgets
from pygame.locals import *
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()

def settings():
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Settings")
    background_screen = pygame.image.load('background.jpeg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    slider = Slider(screen, 1700, 200, 300, 20, min=0, max=100, step=1)
    output = TextBox(screen, 1600, 185, 65, 50, fontSize=30)

    output.disable()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        output.setText(str(slider.getValue()))

        pygame_widgets.update(event)
        pygame.display.update()
        
        screen.blit(background_screen, (0, 0))
        pygame.display.flip()


