import pygame
from pygame.locals import *
import staryinsh_home as menu
import staryinsh_game as game

def victory_screen(winner,mode,type_game):
    # Initializing the window
    pygame.init()
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Menu")

    # Loading the background image
    if winner == 1:
        background_screen = pygame.image.load('images/victory_player1.jpg')
    else:
        background_screen = pygame.image.load('images/victory_player2.jpg')    
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Loading the images
    replay_button_image = pygame.image.load('images/replay.png')
    back_to_home_image = pygame.image.load('images/back_to_home.png')
    
    # Resizing the images
    replay_button_image = pygame.transform.scale(replay_button_image, (315*width_ratio, 150*height_ratio))
    back_to_home_image = pygame.transform.scale(back_to_home_image, (645*width_ratio, 180*height_ratio))

    # Initializing variables
    hover_replay = False
    hover_back = False
    running = True
    
    # Handling events
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 550*width_ratio <= event.pos[0] <= 835*width_ratio and 852*height_ratio <= event.pos[1] <= 959*height_ratio:
                        play_sound()
                        game.launch_game(mode,type_game)
                    if 919*width_ratio <= event.pos[0] <= 1498*width_ratio and 853*height_ratio <= event.pos[1] <= 960*height_ratio:
                        play_sound()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('sounds/menu.mp3')
                        pygame.mixer.music.play(-1)
                        menu.menu()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hover_replay = 535*width_ratio <= x <= 535*width_ratio + replay_button_image.get_width() and 830*height_ratio <= y <= 830*height_ratio + replay_button_image.get_height()
                hover_back = 919*width_ratio <= x <= 855*width_ratio + back_to_home_image.get_width() and 850*height_ratio <= y <= 780*height_ratio + back_to_home_image.get_height()

        
        screen.blit(background_screen, (0, 0))
        
        # Displaying buttons to place them correctly on the screen
        if hover_replay:
            menu.hover(replay_button_image, 532*width_ratio, 820*height_ratio, screen)
        else:
            menu.unhover(replay_button_image, 535*width_ratio, 830*height_ratio, screen)
        if hover_back:
            menu.hover(back_to_home_image, 882*width_ratio, 805*height_ratio, screen)
        else:
            menu.unhover(back_to_home_image, 885*width_ratio, 815*height_ratio, screen)
            
       
        pygame.display.flip()

    pygame.quit()
              
def play_sound():
    sound = pygame.mixer.Sound(f'sounds/button.mp3')
    sound.play()
