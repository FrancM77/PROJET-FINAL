import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.board = [[0 for i in range(10)] for j in range(10)]
        self.player = 1
        self.nb_pieces_placed = 0
        self.piece_image_p1 = pygame.image.load("./pion/pion_j1.png")
        self.piece_image_p1 = pygame.transform.scale(self.piece_image_p1, (80, 80))
        self.piece_image_p2 = pygame.image.load("./pion/pion_j2.png")
        self.piece_image_p2 = pygame.transform.scale(self.piece_image_p2, (80, 80))
        

    def change_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def click_hit_box(self, x, y, x2, y2, event, square_size, screen, i, j):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
                    if self.board[j][i] == 0:
                        self.nb_pieces_placed += 1
                        if self.player == 1:
                            screen.blit(self.piece_image_p1, (x2-40, y2-43))
                            self.board[j][i] = 1
                        else:
                            screen.blit(self.piece_image_p2, (x2-40, y2-43))
                            self.board[j][i] = 2
                        self.change_player()
                        return True
        return False
    
    def show_board(self):
        for row in self.board:
            print(row)
            
    def play(self):
        pygame.init()
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Menu")
        width_ratio = screen_width / 2048
        height_ratio = screen_height / 1152

        background = pygame.image.load('constellation.jpeg')
        background = pygame.transform.scale(background, (screen_width, screen_height))

        running = True
        screen.blit(background, (0, 0))
        square_size = 50
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    from menu_staryinsh import menu
                    menu()
                for i in range(4):
                    j=0
                    self.click_hit_box((697+(i*75))*width_ratio, (190-(i*43))*height_ratio, (723+(i*75))*width_ratio, (215-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(7):
                    j=1
                    self.click_hit_box((622+(i*75))*width_ratio, (320-(i*43))*height_ratio, (649+(i*75))*width_ratio, (345-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(8):
                    j=2
                    self.click_hit_box((622+(i*75))*width_ratio, (405-(i*43))*height_ratio, (649+(i*75))*width_ratio, (435-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(9):
                    j=3
                    self.click_hit_box((622+(i*75))*width_ratio, (495-(i*43))*height_ratio, (647+(i*75))*width_ratio, (520-(i*43))*height_ratio, event, square_size, screen,i,j)      
                for i in range(10):
                    j=4
                    self.click_hit_box((622+(i*75))*width_ratio, (580-(i*43))*height_ratio, (647+(i*75))*width_ratio, (605-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(9):
                    j=5
                    self.click_hit_box((697+(i*75))*width_ratio, (625-(i*43))*height_ratio, (723+(i*75))*width_ratio, (650-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(10): 
                    j=6
                    self.click_hit_box((697+(i*75))*width_ratio, (712-(i*43))*height_ratio, (723+(i*75))*width_ratio, (737-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(9):
                    j=7
                    self.click_hit_box((773+(i*75))*width_ratio, (755-(i*43))*height_ratio, (799+(i*75))*width_ratio, (780-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(8):
                    j=8
                    self.click_hit_box((848+(i*75))*width_ratio, (800-(i*43))*height_ratio, (873+(i*75))*width_ratio, (825-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(7):
                    j=9
                    self.click_hit_box((925+(i*75))*width_ratio, (842-(i*43))*height_ratio, (950+(i*75))*width_ratio, (867-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(4):
                    j=10
                    self.click_hit_box((1075+(i*75))*width_ratio, (843-(i*43))*height_ratio, (1100+(i*75))*width_ratio, (867-(i*43))*height_ratio, event, square_size, screen,i,j)
                    
                pygame.display.flip()
                
                if self.nb_pieces_placed==10:
                    self.show_board()
                    running = False
        pygame.quit()


def launch_game():
    game = Game()
    game.play()



