import pygame
from pygame.locals import *
from jeu_staryinsh import launch_game


pygame.init()

def mode_de_jeu():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mode de jeu")

    # Loading the background image
    background_screen = pygame.image.load('normal_blitz.jpg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Loading the images
    normal_button_image = pygame.image.load('normal_button.png')
    blitz_button_image = pygame.image.load('blitz_button.png')
    
    # Resizing the images
    normal_button_image = pygame.transform.scale(normal_button_image, (505*width_ratio, 260*height_ratio))
    blitz_button_image = pygame.transform.scale(blitz_button_image, (507*width_ratio, 260*height_ratio))

    # Initializing variables
    hover_normal = False
    hover_blitz = False
    running = True
    
    # Handling events
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from menu_staryinsh import menu
                menu()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 865*width_ratio <= event.pos[0] <= 1350*width_ratio and 530*height_ratio <= event.pos[1] <= 764*height_ratio:
                        normal()
                    if 1383*width_ratio <= event.pos[0] <= 1869*width_ratio and 530*height_ratio <= event.pos[1] <= 764*height_ratio:
                        blitz()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hover_normal = 865*width_ratio <= x <= 865*width_ratio + normal_button_image.get_width() and 530*height_ratio <= y <= 530*height_ratio + normal_button_image.get_height()
                hover_blitz = 1383*width_ratio <= x <= 1383*width_ratio + blitz_button_image.get_width() and 530*height_ratio <= y <= 530*height_ratio + blitz_button_image.get_height()

        screen.blit(background_screen, (0, 0))
        
        
        # Displaying buttons to place them correctly on the screen
        if hover_normal:
            hover(normal_button_image, 850*width_ratio, 510*height_ratio, screen)
        else:
            unhover(normal_button_image, 853*width_ratio, 514*height_ratio, screen)
        if hover_blitz:
            hover(blitz_button_image, 1370*width_ratio, 514*height_ratio, screen)
        else:
            unhover(blitz_button_image, 1375*width_ratio, 518*height_ratio, screen)
            
        pygame.display.flip()

    pygame.quit()
    

def normal():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mode de jeu")

    # Loading the background image
    background_screen = pygame.image.load('normal.jpg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Loading the images
    network_button = pygame.image.load('reseau.png')
    ia_button = pygame.image.load('ia.png')
    
    # Resizing the images
    network_button = pygame.transform.scale(network_button, (505*width_ratio, 264*height_ratio))
    ia_button = pygame.transform.scale(ia_button, (508*width_ratio, 263*height_ratio))

    # Initializing variables
    hover_network = False
    hover_ia = False
    running = True
    
    # Handling events
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_de_jeu()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 860*width_ratio <= event.pos[0] <= 1355*width_ratio and 587*height_ratio <= event.pos[1] <= 829*height_ratio:
                        launch_game()
                    if 1380*width_ratio <= event.pos[0] <= 1875*width_ratio and 587*height_ratio <= event.pos[1] <= 829*height_ratio:
                        launch_game()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hover_network = 855*width_ratio <= x <= 855*width_ratio + network_button.get_width() and 570*height_ratio <= y <= 570*height_ratio + network_button.get_height()
                hover_ia = 1365*width_ratio <= x <= 1365*width_ratio + ia_button.get_width() and 570*height_ratio <= y <= 570*height_ratio + ia_button.get_height()

        screen.blit(background_screen, (0, 0))
        
        
        # Displaying buttons to place them correctly on the screen
        if hover_network:
            hover(network_button, 850*width_ratio, 570*height_ratio, screen)
        else:
            unhover(network_button, 855*width_ratio, 575*height_ratio, screen)
        if hover_ia:
            hover(ia_button, 1365*width_ratio, 570*height_ratio, screen)
        else:
            unhover(ia_button, 1370*width_ratio, 575*height_ratio, screen)
            
        pygame.display.flip()

    pygame.quit()
    

def blitz():
    # Initializing the window
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mode de jeu")

    # Loading the background image
    background_screen = pygame.image.load('blitz.jpg')
    background_screen = pygame.transform.scale(background_screen, (screen_width, screen_height))
    
    width_ratio = screen_width / 2048
    height_ratio = screen_height / 1152
    
    # Loading the images
    network_button = pygame.image.load('reseau.png')
    ia_button = pygame.image.load('ia.png')
    
    # Resizing the images
    network_button = pygame.transform.scale(network_button, (505*width_ratio, 264*height_ratio))
    ia_button = pygame.transform.scale(ia_button, (508*width_ratio, 263*height_ratio))

    # Initializing variables
    hover_network = False
    hover_ia = False
    running = True
    
    # Handling events
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_de_jeu()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 860*width_ratio <= event.pos[0] <= 1355*width_ratio and 587*height_ratio <= event.pos[1] <= 829*height_ratio:
                        launch_game()
                    if 1380*width_ratio <= event.pos[0] <= 1875*width_ratio and 587*height_ratio <= event.pos[1] <= 829*height_ratio:
                        launch_game()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hover_network = 855*width_ratio <= x <= 855*width_ratio + network_button.get_width() and 570*height_ratio <= y <= 570*height_ratio + network_button.get_height()
                hover_ia = 1365*width_ratio <= x <= 1365*width_ratio + ia_button.get_width() and 570*height_ratio <= y <= 570*height_ratio + ia_button.get_height()

        screen.blit(background_screen, (0, 0))
        
        
        
        # Displaying buttons to place them correctly on the screen
        if hover_network:
            hover(network_button, 850*width_ratio, 570*height_ratio, screen)
        else:
            unhover(network_button, 855*width_ratio, 575*height_ratio, screen)
        if hover_ia:
            hover(ia_button, 1365*width_ratio, 570*height_ratio, screen)
        else:
            unhover(ia_button, 1370*width_ratio, 575*height_ratio, screen)
            
        pygame.display.flip()

    pygame.quit()

    
def hover(img,x,y,screen):
    screen.blit(pygame.transform.scale(img, (img.get_width()+10, img.get_height() + 10)), (x, y))

def unhover(img,x,y,screen):
    pygame.time.wait(20)
    screen.blit(img, (x,y))   





