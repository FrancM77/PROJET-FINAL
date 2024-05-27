import pygame
from pygame.locals import *
from staryinsh_game import launch_game

class GameMode:
    '''
    This class is used to display the game mode screen.
    '''
    def __init__(self):
        '''
        This function initializes the game mode screen.
        '''
        pygame.init()
        # Initializing the window
        self.screen_width, self.screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Mode")
        self.background_screen = pygame.image.load('images/normal_blitz.jpg')
        self.background_screen = pygame.transform.scale(self.background_screen, (self.screen_width, self.screen_height))
        self.width_ratio = self.screen_width / 2048
        self.height_ratio = self.screen_height / 1152
        
        # Loading the images
        self.normal_button_image = pygame.transform.scale(pygame.image.load('images/normal_button.png'), (int(505*self.width_ratio), int(260*self.height_ratio)))
        self.blitz_button_image = pygame.transform.scale(pygame.image.load('images/blitz_button.png'), (int(507*self.width_ratio), int(260*self.height_ratio)))
        
        # Initializing variables
        self.running = True
        self.hover_normal = False
        self.hover_blitz = False

    def run(self):
        '''
        This function runs the game mode screen.
        '''
        from staryinsh_home import play_button_sound
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    from staryinsh_home import menu
                    menu()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 865*self.width_ratio <= event.pos[0] <= 1350*self.width_ratio and 530*self.height_ratio <= event.pos[1] <= 764*self.height_ratio:
                            play_button_sound()
                            self.choose_mode("normal")
                        if 1383*self.width_ratio <= event.pos[0] <= 1869*self.width_ratio and 530*self.height_ratio <= event.pos[1] <= 764*self.height_ratio:
                            play_button_sound()
                            self.choose_mode("blitz")
                elif event.type == MOUSEMOTION:
                    self.handle_mouse_motion(event.pos)

            self.screen.blit(self.background_screen, (0, 0))
            self.update_button_display()
            pygame.display.flip()

        pygame.quit()
    
    def choose_mode(self, mode):
        '''
        This function launches the game mode chosen by the player.
        
        params:
        mode: the mode chosen by the player , type: str
        '''
        if mode == "normal" or mode == "blitz":
            Mode(self.screen, mode, self.screen_width, self.screen_height, self.width_ratio, self.height_ratio).run()

    def handle_mouse_motion(self, pos):
        '''
        This function handles the mouse motion on the screen.
        
        params:
        pos: the position of the mouse , type: tuple
        '''
        x, y = pos
        self.hover_normal = 865*self.width_ratio <= x <= 1350*self.width_ratio and 530*self.height_ratio <= y <= 764*self.height_ratio
        self.hover_blitz = 1383*self.width_ratio <= x <= 1869*self.width_ratio and 530*self.height_ratio <= y <= 764*self.height_ratio

    def update_button_display(self):
        '''
        This function updates the display of the buttons.
        '''
        if self.hover_normal:
            self.hover(self.normal_button_image, 850*self.width_ratio, 510*self.height_ratio)
        else:
            self.unhover(self.normal_button_image, 853*self.width_ratio, 514*self.height_ratio)
        if self.hover_blitz:
            self.hover(self.blitz_button_image, 1370*self.width_ratio, 514*self.height_ratio)
        else:
            self.unhover(self.blitz_button_image, 1375*self.width_ratio, 518*self.height_ratio)

    def hover(self, img, x, y):
        '''
        This function displays the hovered image at the given coordinates.
        
        params:
        img: the image to display , type: pygame.Surface
        x: the x-coordinate , type: int
        y: the y-coordinate , type: int
        '''
        self.screen.blit(pygame.transform.scale(img, (img.get_width()+10, img.get_height() + 10)), (x, y))

    def unhover(self, img, x, y):
        '''
        This function displays the unhovered image at the given coordinates.
        
        params:
        img: the image to display , type: pygame.Surface
        x: the x-coordinate , type: int
        y: the y-coordinate , type: int
        '''
        pygame.time.wait(20)
        self.screen.blit(img, (x,y))

class Mode:
    '''
    This class is used to display the mode screen.
    '''
    def __init__(self, screen, mode, screen_width, screen_height, width_ratio, height_ratio):
        '''
        This function initializes the mode screen.
        
        params:
        screen: the screen to display the mode on , type: pygame.Surface
        mode: the mode chosen by the player , type: str
        screen_width: the width of the screen , type: int
        screen_height: the height of the screen , type: int
        width_ratio: the width ratio , type: float
        height_ratio: the height ratio , type: float
        '''
        self.screen = screen
        self.mode = mode
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.background_image_path = f'images/{mode}.jpg'
        self.local_button = pygame.transform.scale(pygame.image.load('images/local.png'), (int(505*width_ratio), int(264*height_ratio)))
        self.ia_button = pygame.transform.scale(pygame.image.load('images/ai.png'), (int(508*width_ratio), int(263*height_ratio)))

    def run(self):
        '''
        This function runs the mode screen.
        '''
        from staryinsh_home import play_button_sound
        hover_local = False
        hover_ia = False
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 860*self.width_ratio <= event.pos[0] <= 1355*self.width_ratio and 587*self.height_ratio <= event.pos[1] <= 829*self.height_ratio:
                            play_button_sound()
                            launch_game(self.mode, "local")
                        if 1380*self.width_ratio <= event.pos[0] <= 1875*self.width_ratio and 587*self.height_ratio <= event.pos[1] <= 829*self.height_ratio:
                            play_button_sound()
                            launch_game(self.mode, "AI")
                elif event.type == MOUSEMOTION:
                    hover_local = 855*self.width_ratio <= event.pos[0] <= 855*self.width_ratio + self.local_button.get_width() and 570*self.height_ratio <= event.pos[1] <= 570*self.height_ratio + self.local_button.get_height()
                    hover_ia = 1365*self.width_ratio <= event.pos[0] <= 1365*self.width_ratio + self.ia_button.get_width() and 570*self.height_ratio <= event.pos[1] <= 570*self.height_ratio + self.ia_button.get_height()

            self.screen.blit(pygame.transform.scale(pygame.image.load(self.background_image_path), (self.screen_width, self.screen_height)), (0, 0))
            if hover_local:
                GameMode.hover(self,self.local_button, 850*self.width_ratio, 570*self.height_ratio)
            else:
                GameMode.unhover(self,self.local_button, 855*self.width_ratio, 575*self.height_ratio)
            if hover_ia:
                GameMode.hover(self,self.ia_button, 1365*self.width_ratio, 570*self.height_ratio)
            else:
                GameMode.unhover(self,self.ia_button, 1370*self.width_ratio, 575*self.height_ratio)
            pygame.display.flip()

