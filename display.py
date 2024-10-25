import pygame
from pygame.locals import *

class Display:
    '''
    This class is used to display the game on the screen.
    '''
    def __init__(self,game,width_ratio,height_ratio,piece_image):
        '''
        This function initializes the display object.
        
        params:
        game: the game object , type: Game
        width_ratio: the width ratio , type: float
        height_ratio: the height ratio , type: float
        piece_image: the image of the piece , type: pygame.Surface
        '''
        self.game = game
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.piece_image = piece_image


    def display_piece(self, screen):
        '''
        This function displays the pieces on the board.
        
        params:
        screen: the screen to display the pieces on , type: pygame.Surface
        '''
        self.load_background(screen)
        piece_data = [
            (1, 5, 265),
            (0, 7, 345),
            (0, 8, 435),
            (0, 9, 520),
            (0, 10, 605),
            (1, 10, 695),
            (1, 11, 782),
            (2, 11, 870),
            (3, 11, 957),
            (4, 11, 1043),
            (5, 11, 1130)
            ]
        for j, (start, end, y_coor) in enumerate(piece_data):
            for i in range(start, end):
                self.display_piece_action((649 + (i * 75) - 31) * self.width_ratio, (y_coor - (i * 43) - 35) * self.height_ratio, screen, i, j)

    
    def display_piece_action(self, x2, y2, screen, i, j):
        '''
        This function displays the pieces on the board.
        
        params:
        x2: the x-coordinate of the piece , type: int
        y2: the y-coordinate of the piece , type: int
        screen: the screen to display the pieces on , type: pygame.Surface
        i: the x-coordinate of the piece on the board , type: int
        j: the y-coordinate of the piece on the board , type: int
        '''
        self.display_side_piece_start(screen)
        self.display_points(screen)
        if self.game.board[j][i] == 1:
            screen.blit(self.piece_image[1], (x2, y2))
        elif self.game.board[j][i] == 2:
            screen.blit(self.piece_image[2], (x2, y2))
        elif self.game.board[j][i] == 3:
            screen.blit(self.piece_image[3], (x2, y2))
        elif self.game.board[j][i] == 4:
            screen.blit(self.piece_image[4], (x2, y2))
        elif self.game.board[j][i] == 5:
            screen.blit(self.piece_image[5], (x2, y2))
        elif self.game.board[j][i] == 6:
            screen.blit(self.piece_image[6], (x2, y2))
            
    
    def load_side_img(self,number,alpha,x,y,screen):
        '''
        This function loads the images on the sides of the board.
        
        params:
        number: the number of the image , type: int
        alpha: the alpha value of the image , type: int
        x: the x-coordinate of the image , type: int
        y: the y-coordinate of the image , type: int
        screen: the screen to display the image on , type: pygame.Surface
        
        return:
        the image loaded on the screen , type: pygame.Surface
        '''
        image = self.piece_image[number].convert_alpha()
        image.set_alpha(alpha)
        image = pygame.transform.scale(image, (100*self.width_ratio, 100*self.height_ratio))
        screen.blit(image, (x*self.width_ratio, y*self.height_ratio))
        return image
    
    def display_points(self, screen):
        '''
        This function displays the points on the sides of the board.
        
        params:
        screen: the screen to display the points on , type: pygame.Surface
        '''
        for i in range(self.game.player_1_points):
            self.load_side_img(1,256,10,(10+(i*95)),screen)
        for i in range(self.game.player_2_points):
            self.load_side_img(2,256,1940,(1050-(i*95)),screen)
                    
    def display_side_piece_start(self,screen):
        '''
        This function displays the starting pieces on the sides of the board.
        
        params:
        screen: the screen to display the starting pieces on , type: pygame.Surface
        '''
        for i in range(self.game.nb_circle):
            self.load_side_img(1,2,10,(10+(i*95)),screen)
            self.load_side_img(2,3,1940,(1050-(i*95)),screen)


    def display_player(self, screen):
        '''
        This function displays the player images on the screen.

        params:
        screen: the screen to display the player images on , type: pygame.Surface
        '''
        player1_ship = pygame.transform.scale(pygame.image.load('images/pink_ship.png'), (550*self.width_ratio, 375*self.height_ratio))
        player2_ship = pygame.transform.scale(pygame.image.load('images/green_ship.png'), (375*self.width_ratio, 300*self.height_ratio))
        None if self.game.type == "AI" else screen.blit(player1_ship, (10*self.width_ratio, 500*self.height_ratio)) if self.game.player == 1 else screen.blit(player2_ship, (1500*self.width_ratio, 500*self.height_ratio))
         
            
    def load_background(self, screen):
        '''
        This function loads the background image on the screen.
        
        params:
        screen: the screen to display the background on , type: pygame.Surface
        '''
        background = pygame.image.load('images/board.jpeg')
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.blit(background, (0, 0))     


    def display_info(self, screen, font):
        '''
        This function displays the information on the screen.
        
        params:
        screen: the screen to display the information on , type: pygame.Surface
        font: the font of the text , type: pygame.font.Font
        '''
        RGB = (235,117,141) if self.game.player == 1 else (84, 181, 97)
        while self.game.nb_pieces_placed_depart < 10:
            if self.game.type == "AI":
                text = font.render(f"Veuillez placer un de vos 5 pions", True, RGB)
                screen.blit(text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                text = font.render(f"Joueur {self.game.player}, veuillez placer un de vos 5 pions", True, RGB)
                screen.blit(text, (550*self.width_ratio, 900*self.height_ratio))
            return
        if self.game.multialign:
            if self.game.type == "AI":
                multialign_text = font.render(f"Veuillez supprimer un de vos alignements", True, RGB)
                screen.blit(multialign_text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                multialign_text = font.render(f"Joueur {self.game.player}, veuillez supprimer un de vos alignements", True, RGB)
                screen.blit(multialign_text, (470*self.width_ratio, 900*self.height_ratio))
            return
        elif self.game.remove_mode:
            if self.game.type == "AI":
                remove_text = font.render(f"Veuillez supprimer un de vos pions", True, RGB)
                screen.blit(remove_text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                remove_text = font.render(f"Joueur {self.game.player}, veuillez supprimer un de vos pions", True, RGB)
                screen.blit(remove_text, (550*self.width_ratio, 900*self.height_ratio))
            return 
        elif self.game.type == "AI":
            player_text = font.render(f"C'est à votre tour", True, RGB)
            screen.blit(player_text, (800*self.width_ratio, 900*self.height_ratio)) 
        else:
            player_text = font.render(f"C'est au tour du joueur {self.game.player}", True, RGB)
            screen.blit(player_text, (750*self.width_ratio, 900*self.height_ratio)) 