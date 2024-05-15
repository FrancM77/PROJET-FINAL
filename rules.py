import pygame
from pygame.locals import *
import os

def load_images(screen_width, screen_height):
    images_folder = 'img_rules'
    image_files = os.listdir(images_folder)
    images = [pygame.image.load(os.path.join(images_folder, img)) for img in image_files]
    images = [pygame.transform.scale(img, (screen_width, screen_height)) for img in images]
    return images

def rules():
    pygame.init()
    
    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Rules")
    
    rule_image = pygame.image.load('img_rules/rules1.jpg')
    rule_image = pygame.transform.scale(rule_image, (screen_width, screen_height))
    screen.blit(rule_image, (0, 0))
    pygame.display.flip()

    images = load_images(screen_width, screen_height)

    carousel_x_position = 0
    current_image_index = 0

    left_button_margin = 0.655
    right_button_margin = 0.48
    bottom_button_margin = 0.2

    button_width = int(screen_width * 0.15)
    button_height = int(screen_height * 0.1)

    next_button = pygame.transform.scale(pygame.image.load('images/next_button.png'), (button_width, button_height))
    previous_button = pygame.transform.scale(pygame.image.load('images/previous_button.png'), (button_width, button_height))

    running = True
    
    from staryinsh_home import play_button_sound
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from staryinsh_home import menu
                menu()
                return
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                hovering_over_previous_button = screen_width - screen_width * left_button_margin <= x <= screen_width - screen_width * left_button_margin + button_width and screen_height - screen_height * bottom_button_margin <= y <= screen_height - screen_height * bottom_button_margin + button_height
                hovering_over_next_button = screen_width - screen_width * right_button_margin <= x <= screen_width - screen_width * right_button_margin + button_width and screen_height - screen_height * bottom_button_margin <= y <= screen_height - screen_height * bottom_button_margin + button_height

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if hovering_over_next_button:
                        play_button_sound()
                        current_image_index = (current_image_index + 1) % len(images)
                        carousel_x_position = -current_image_index * screen_width
                    elif hovering_over_previous_button:
                        play_button_sound()
                        current_image_index = (current_image_index - 1) % len(images)
                        carousel_x_position = -current_image_index * screen_width

        for i, image in enumerate(images):
            image_x_position = i * screen_width + carousel_x_position
            transition_x = max(0, min(screen_width, image_x_position))
            screen.blit(image, (transition_x, 0))

        if hovering_over_next_button:
            screen.blit(pygame.transform.scale(next_button, (next_button.get_width() + 15, next_button.get_height() + 15)), (screen_width - screen_width * right_button_margin - 7, screen_height - screen_height * bottom_button_margin - 7))
        else:
            screen.blit(next_button, (screen_width - screen_width * right_button_margin, screen_height - screen_height * bottom_button_margin))

        if hovering_over_previous_button:
            screen.blit(pygame.transform.scale(previous_button, (previous_button.get_width() + 15, previous_button.get_height() + 15)), (screen_width - screen_width * left_button_margin - 7, screen_height - screen_height * bottom_button_margin - 7))
        else:
            screen.blit(previous_button, (screen_width - screen_width * left_button_margin, screen_height - screen_height * bottom_button_margin))

        pygame.display.flip()

    pygame.quit()


