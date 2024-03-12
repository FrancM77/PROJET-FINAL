import pygame
from pygame.locals import *
import image_carousel as rules
import staryinsh_game as game
import staryinsh_settings as settings

pygame.init()

def menu():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Menu")

    # Loading the background image
    background_screen = pygame.image.load('background.jpeg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Loading the images
    start_button_image = pygame.image.load('start.jpg')
    rules_button_image = pygame.image.load('rules.jpg')
    settings_button_image = pygame.image.load('settings.jpg')
    
    # Resizing the images
    start_button_image = pygame.transform.scale(start_button_image, (800*width_ratio, 700*height_ratio))
    rules_button_image = pygame.transform.scale(rules_button_image, (800*width_ratio, 350*height_ratio))
    settings_button_image = pygame.transform.scale(settings_button_image, (800*width_ratio, 350*height_ratio))

    # Initializing variables
    hover_start = False
    hover_rules = False
    hover_settings = False
    running = True
    
    # Handling events
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 1046*width_ratio <= event.pos[0] <= 1796*width_ratio and 200*height_ratio <= event.pos[1] <= 550*height_ratio:
                        rules.carousel()
                    if 250*width_ratio <= event.pos[0] <= 1050*width_ratio and 200*height_ratio <= event.pos[1] <= 900*height_ratio:
                        game.launch_game()
                    if 1046*width_ratio <= event.pos[0] <= 1646*width_ratio and 549*height_ratio <= event.pos[1] <= 899*height_ratio:
                        settings.settings()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hover_start = 250*width_ratio <= x <= 250*width_ratio + start_button_image.get_width() and 200*height_ratio <= y <= 200*height_ratio + start_button_image.get_height()
                hover_rules = 1046*width_ratio <= x <= 1046*width_ratio + rules_button_image.get_width() and 200*height_ratio <= y <= 200*height_ratio + rules_button_image.get_height()
                hover_settings = 1046*width_ratio <= x <= 1046*width_ratio + settings_button_image.get_width() and 549*height_ratio <= y <= 549*height_ratio + settings_button_image.get_height()

        screen.blit(background_screen, (0, 0))
        
        
        # Displaying buttons to place them correctly on the screen
        if hover_start:
            screen.blit(pygame.transform.scale(start_button_image, (start_button_image.get_width() + 15, start_button_image.get_height() + 15)), (245*width_ratio, 195*height_ratio))
        else:
            pygame.time.wait(20)
            screen.blit(start_button_image, (250*width_ratio, 200*height_ratio))

        if hover_rules:
            screen.blit(pygame.transform.scale(rules_button_image, (rules_button_image.get_width() + 15, rules_button_image.get_height() + 15)), (1046*width_ratio, 190*height_ratio))
        else:
            pygame.time.wait(20)
            screen.blit(rules_button_image, (1046*width_ratio, 200*height_ratio))

        if hover_settings:
            screen.blit(pygame.transform.scale(settings_button_image, (settings_button_image.get_width() + 15, settings_button_image.get_height() + 15)), (1046*width_ratio, 549*height_ratio))
        else:
            pygame.time.wait(20)
            screen.blit(settings_button_image, (1046*width_ratio, 549*height_ratio))
            

        pygame.display.flip()

    pygame.quit()

menu()
