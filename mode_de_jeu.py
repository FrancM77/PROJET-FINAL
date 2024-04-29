import pygame
from pygame.locals import *
from jeu_staryinsh import launch_game

class ModeDeJeu:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Mode de jeu")
        self.background_screen = pygame.image.load('normal_blitz.jpg')
        self.background_screen = pygame.transform.scale(self.background_screen, (self.screen_width, self.screen_height))
        self.width_ratio = self.screen_width / 2048
        self.height_ratio = self.screen_height / 1152
        self.normal_button_image = pygame.transform.scale(pygame.image.load('normal_button.png'), (int(505*self.width_ratio), int(260*self.height_ratio)))
        self.blitz_button_image = pygame.transform.scale(pygame.image.load('blitz_button.png'), (int(507*self.width_ratio), int(260*self.height_ratio)))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 865*self.width_ratio <= event.pos[0] <= 1350*self.width_ratio and 530*self.height_ratio <= event.pos[1] <= 764*self.height_ratio:
                            self.choose_mode("normal")
                        if 1383*self.width_ratio <= event.pos[0] <= 1869*self.width_ratio and 530*self.height_ratio <= event.pos[1] <= 764*self.height_ratio:
                            self.choose_mode("blitz")
                elif event.type == MOUSEMOTION:
                    self.handle_mouse_motion(event.pos)

            self.screen.blit(self.background_screen, (0, 0))
            self.update_button_display()
            pygame.display.flip()

        pygame.quit()

    def choose_mode(self, mode):
        if mode == "normal" or mode == "blitz":
            Mode(self.screen, mode, self.screen_width, self.screen_height, self.width_ratio, self.height_ratio).run()

    def handle_mouse_motion(self, pos):
        x, y = pos
        self.hover_normal = 865*self.width_ratio <= x <= 1350*self.width_ratio and 530*self.height_ratio <= y <= 764*self.height_ratio
        self.hover_blitz = 1383*self.width_ratio <= x <= 1869*self.width_ratio and 530*self.height_ratio <= y <= 764*self.height_ratio

    def update_button_display(self):
        if self.hover_normal:
            self.hover(self.normal_button_image, 850*self.width_ratio, 510*self.height_ratio)
        else:
            self.unhover(self.normal_button_image, 853*self.width_ratio, 514*self.height_ratio)
        if self.hover_blitz:
            self.hover(self.blitz_button_image, 1370*self.width_ratio, 514*self.height_ratio)
        else:
            self.unhover(self.blitz_button_image, 1375*self.width_ratio, 518*self.height_ratio)

    def hover(self, img, x, y):
        self.screen.blit(pygame.transform.scale(img, (img.get_width()+10, img.get_height() + 10)), (x, y))

    def unhover(self, img, x, y):
        pygame.time.wait(20)
        self.screen.blit(img, (x,y))

class Mode:
    def __init__(self, screen, mode, screen_width, screen_height, width_ratio, height_ratio):
        self.screen = screen
        self.mode = mode
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.background_image_path = f'{mode}.jpg'
        self.network_button = pygame.transform.scale(pygame.image.load('reseau.png'), (int(505*width_ratio), int(264*height_ratio)))
        self.ia_button = pygame.transform.scale(pygame.image.load('ia.png'), (int(508*width_ratio), int(263*height_ratio)))

    def run(self):
        hover_network = False
        hover_ia = False
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 860*self.width_ratio <= event.pos[0] <= 1355*self.width_ratio and 587*self.height_ratio <= event.pos[1] <= 829*self.height_ratio:
                            launch_game()
                        if 1380*self.width_ratio <= event.pos[0] <= 1875*self.width_ratio and 587*self.height_ratio <= event.pos[1] <= 829*self.height_ratio:
                            launch_game()
                elif event.type == MOUSEMOTION:
                    hover_network = 855*self.width_ratio <= event.pos[0] <= 855*self.width_ratio + self.network_button.get_width() and 570*self.height_ratio <= event.pos[1] <= 570*self.height_ratio + self.network_button.get_height()
                    hover_ia = 1365*self.width_ratio <= event.pos[0] <= 1365*self.width_ratio + self.ia_button.get_width() and 570*self.height_ratio <= event.pos[1] <= 570*self.height_ratio + self.ia_button.get_height()

            self.screen.blit(pygame.transform.scale(pygame.image.load(self.background_image_path), (self.screen_width, self.screen_height)), (0, 0))
            if hover_network:
                self.hover(self.network_button, 850*self.width_ratio, 570*self.height_ratio)
            else:
                self.unhover(self.network_button, 855*self.width_ratio, 575*self.height_ratio)
            if hover_ia:
                self.hover(self.ia_button, 1365*self.width_ratio, 570*self.height_ratio)
            else:
                self.unhover(self.ia_button, 1370*self.width_ratio, 575*self.height_ratio)
            pygame.display.flip()

    def hover(self, img, x, y):
        self.screen.blit(pygame.transform.scale(img, (img.get_width()+10, img.get_height() + 10)), (x, y))

    def unhover(self, img, x, y):
        pygame.time.wait(20)
        self.screen.blit(img, (x,y))

if __name__ == "__main__":
    ModeDeJeu().run()
