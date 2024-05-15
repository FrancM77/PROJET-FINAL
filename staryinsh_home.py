import pygame
from pygame.locals import *
import rules as rules
from gamemode import GameMode

pygame.init()

def menu():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Menu")

    # Loading the background image
    background_screen = pygame.image.load('images/background.jpeg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Loading the images
    start_button_image = pygame.image.load('images/play.jpg')
    rules_button_image = pygame.image.load('images/rules.jpg')
    
    # Resizing the images
    start_button_image = pygame.transform.scale(start_button_image, (800*width_ratio, 700*height_ratio))
    rules_button_image = pygame.transform.scale(rules_button_image, (800*width_ratio, 700*height_ratio))

    # Initializing variables
    hover_start = False
    hover_rules = False
    running = True
    
    # Handling events
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 250*width_ratio <= event.pos[0] <= 1050*width_ratio and 200*height_ratio <= event.pos[1] <= 900*height_ratio:
                        play_button_sound()
                        GameMode().run()
                    if 1046*width_ratio <= event.pos[0] <= 1796*width_ratio and 200*height_ratio <= event.pos[1] <= 900*height_ratio:
                        play_button_sound()
                        rules.rules()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hover_start = 250*width_ratio <= x <= 250*width_ratio + start_button_image.get_width() and 200*height_ratio <= y <= 200*height_ratio + start_button_image.get_height()
                hover_rules = 1046*width_ratio <= x <= 1046*width_ratio + rules_button_image.get_width() and 200*height_ratio <= y <= 200*height_ratio + rules_button_image.get_height()

        screen.blit(background_screen, (0, 0))
        
        
        # Displaying buttons to place them correctly on the screen
        if hover_start:
            hover(start_button_image, 245*width_ratio, 195*height_ratio, screen)
        else:
            unhover(start_button_image, 250*width_ratio, 200*height_ratio, screen)
        if hover_rules:
            hover(rules_button_image, 1046*width_ratio, 190*height_ratio, screen)
        else:
            unhover(rules_button_image, 1046*width_ratio, 200*height_ratio, screen)
            

        pygame.display.flip()

    pygame.quit()
    
def hover(img,x,y,screen):
    screen.blit(pygame.transform.scale(img, (img.get_width()+3, img.get_height() + 15)), (x, y))

def unhover(img,x,y,screen):
    pygame.time.wait(20)
    screen.blit(img, (x,y))           


def play_button_sound():
    sound = pygame.mixer.Sound(f'sounds/button.mp3')
    sound.play()