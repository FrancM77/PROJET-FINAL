import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.board= [ ['N', 0, 0 ,0 ,0, 'N', 'N' ,'N', 'N' ,'N', 'N'],
                    [0, 0, 0 ,0, 0 ,0 ,0, 'N', 'N' ,'N', 'N'],
                    [0, 0 ,0 ,0 ,0, 0, 0 ,0, 'N', 'N' ,'N'] ,
                    [0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 'N' ,'N'],
                    [0, 0 ,0 ,0 ,0 ,0, 0 ,0, 0 ,0 ,'N' ],
                    ['N', 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,'N'] ,
                    ['N', 0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0 ],
                    ['N' ,'N', 0, 0 ,0 ,0 ,0, 0 ,0 ,0 ,0] ,
                    ['N' ,'N', 'N', 0, 0 ,0 ,0 ,0 ,0, 0 ,0],
                    ['N', 'N', 'N', 'N', 0 ,0, 0 ,0, 0 ,0 ,0],
                    ['N', 'N' ,'N', 'N', 'N' ,'N' ,0 ,0, 0 ,0, 'N']]
        
        self.player = 1
        self.nb_pieces_placed_depart = 0
        self.nb_pieces_full_placed = 0
        self.placed_second_piece = False
        self.placed_third_piece = False
        self.previous_position = None
        self.previous_player = None  
        self.piece_image = {}
        for i in range(1,7):
            ratio_height , ratio_len = self.ratio()
            self.piece_image[i] = pygame.image.load(f'./pion/pion{i}.png')
            self.piece_image[i] = pygame.transform.scale(self.piece_image[i], (60*ratio_height, 60*ratio_len))

    def change_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def recover_offset(self,j):
        count = 0
        for row in range(11):
            if self.board[j][row] == 'N':
                count += 1
            elif self.board[j][row] in [0,1, 2, 3, 4, 5, 6]:
                return count
    
    def place_first_piece(self, x, y, event, square_size, screen, i, j):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            if self.board[j][i] == 0:
                self.nb_pieces_placed_depart += 1
                self.board[j][i] = 1 if self.player == 1 else 2
                self.display_piece(screen)
                self.change_player()
        return False
    
    def place_second_piece(self, x, y, event, square_size, screen, i, j):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            if self.player == 1 and self.board[j][i] == 1:
                self.board[j][i] = 5
                self.display_piece(screen)
                return True, (i, j)
            if self.player == 2 and self.board[j][i] == 2:
                self.board[j][i] = 6
                self.display_piece(screen)
                return True, (i, j)
            self.change_player()
        return False, None

   

    def place_third_piece(self, x, y, event, square_size, screen, i, j):
        if self.previous_player == self.player:
            return False
        previous_i , previous_j = self.previous_position
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            if self.is_valid_move(previous_i, previous_j, i, j) and self.board[j][i] == 0:
                self.board[j][i] = 1 if self.player == 1 else 2
                self.display_piece(screen)
                self.board[previous_j][previous_i] = 3 if self.player == 1 else 4
                self.display_piece(screen)
                self.previous_player = self.player
                self.change_player()
                return True
        return False
    
    
    
    def is_valid_move(self, start_x, start_y, end_x, end_y):
        if start_x == end_x or start_y == end_y:
            # colonne (|)
            if start_x == end_x: 
                min_y = min(start_y, end_y)
                max_y = max(start_y, end_y)
                for y in range(min_y + 1, max_y):
                    if self.board[y][start_x] in [1, 2]: 
                        return False
            else: 
                # ligne (-)
                min_x = min(start_x, end_x)
                max_x = max(start_x, end_x)
                for x in range(min_x + 1, max_x):
                    if self.board[start_y][x] in [1, 2]: 
                        return False
            return True
        # Diagonal utile (\)
        if start_x - end_x == start_y - end_y: 
            min_x = min(start_x, end_x)
            max_x = max(start_x, end_x)
            min_y = min(start_y, end_y)
            max_y = max(start_y, end_y)
            for i in range(1, abs(start_x - end_x)):
                x = min_x + i
                y = min_y + i
                if self.board[y][x] in [1, 2]:
                    return False
            return True

        return False


    def align_condition(self):
        for j in range(11):
            for i in range(10):
                # Horizontal (-)
                if i <= 5:
                    if self.board[j][i] in [3, 4]:
                        if self.board[j][i] == self.board[j][i + 1] == self.board[j][i + 2] == self.board[j][i + 3] == self.board[j][i + 4]:
                            for k in range(5):
                                self.board[j][i + k] = 0
                            return True

                # Vertical (|)
                if j <= 6:
                    if self.board[j][i] in [3, 4]:
                        if self.board[j][i] == self.board[j + 1][i] == self.board[j + 2][i] == self.board[j + 3][i] == self.board[j + 4][i]:
                            for k in range(5):
                                self.board[j + k][i] = 0
                            return True

                # Diagonal utile (\)
                if j <= 6 and i <= 5:
                    if self.board[j][i] in [3, 4]:
                        if self.board[j][i] == self.board[j + 1][i + 1] == self.board[j + 2][i + 2] == self.board[j + 3][i + 3] == self.board[j + 4][i + 4]:
                            for k in range(5):
                                self.board[j + k][i + k] = 0    
                            return True
        return False

    
    def piece_action(self, x, y, event, square_size, screen, i, j):
        if self.nb_pieces_placed_depart < 2:
            return self.place_first_piece(x, y, event, square_size, screen, i, j)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.place_third_piece(x, y, event, square_size, screen, i, j)
                if self.placed_third_piece:
                    self.nb_pieces_full_placed += 1
                    self.placed_second_piece = False
                    self.previous_position = None
            else:
                self.placed_second_piece, self.previous_position = self.place_second_piece(x, y,event, square_size, screen, i, j)
        
        return False

        

    def display_piece(self,screen):
        self.load_background(screen)
        for i in range(1,5):
            j=0
            self.display_piece_action(649+(i*75)-31, 265-(i*43)-35,screen,i,j)
        for i in range(7):
            j=1
            self.display_piece_action(649+(i*75)-31, 345-(i*43)-35,screen,i,j)
        for i in range(8):
            j=2
            self.display_piece_action(649+(i*75)-31, 435-(i*43)-35,screen,i,j)
        for i in range(9):
            j=3
            self.display_piece_action(647+(i*75)-31, 520-(i*43)-35,screen,i,j)    
        for i in range(10):
            j=4
            self.display_piece_action(647+(i*75)-31, 605-(i*43)-35,screen,i,j)
        for i in range(1,10):
            j=5
            self.display_piece_action(649+(i*75)-31, 695-(i*43)-35,screen,i,j)
        for i in range(1,11): 
            j=6
            self.display_piece_action(649+(i*75)-31, 782-(i*43)-35,screen,i,j)
        for i in range(2,11):
            j=7
            self.display_piece_action(649+(i*75)-31, 870-(i*43)-35,screen,i,j)
        for i in range(3,11):
            j=8
            self.display_piece_action(650+(i*75)-31, 957-(i*43)-35,screen,i,j)
        for i in range(4,11):
            j=9
            self.display_piece_action(650+(i*75)-31, 1043-(i*43)-35,screen,i,j)
        for i in range(5,11):
            j=10
            self.display_piece_action(650+(i*75)-31, 1130-(i*43)-35,screen,i,j)
    
    def load_background(self, screen):
        background = pygame.image.load('constellation.jpeg')
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.blit(background, (0, 0))     
            
    def display_piece_action(self, x2, y2, screen, i, j): 
        if self.board[j][i] == 1:
            screen.blit(self.piece_image[1], (x2, y2))
        elif self.board[j][i] == 2:
            screen.blit(self.piece_image[2], (x2, y2))
        elif self.board[j][i] == 3:
            screen.blit(self.piece_image[3], (x2, y2))
        elif self.board[j][i] == 4:
            screen.blit(self.piece_image[4], (x2, y2))
        elif self.board[j][i] == 5:
            screen.blit(self.piece_image[5], (x2, y2))
        elif self.board[j][i] == 6:
            screen.blit(self.piece_image[6], (x2, y2))
        

    def hit_box(self, event, square_size, screen,width_ratio, height_ratio):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(4):
                    j=0
                    self.piece_action((697+(i*75))*width_ratio, (190-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(7):
                    j=1
                    self.piece_action((622+(i*75))*width_ratio, (320-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(8):
                    j=2
                    self.piece_action((622+(i*75))*width_ratio, (405-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(9):
                    j=3
                    self.piece_action((622+(i*75))*width_ratio, (495-(i*43))*height_ratio, event, square_size, screen,i,j)      
                for i in range(10):
                    j=4
                    self.piece_action((622+(i*75))*width_ratio, (580-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(9):
                    j=5
                    self.piece_action((697+(i*75))*width_ratio, (625-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(10): 
                    j=6
                    self.piece_action((697+(i*75))*width_ratio, (712-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(9):
                    j=7
                    self.piece_action((773+(i*75))*width_ratio, (755-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(8):
                    j=8
                    self.piece_action((848+(i*75))*width_ratio, (800-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(7):
                    j=9
                    self.piece_action((925+(i*75))*width_ratio, (842-(i*43))*height_ratio, event, square_size, screen,i,j)
                for i in range(4):
                    j=10
                    self.piece_action((1075+(i*75))*width_ratio, (843-(i*43))*height_ratio, event, square_size, screen,i,j)    
        
    def show_board(self):
        for i in range(11):
            for j in range(10):
                print(self.board[i][j], end=" ")
            print()
    
    def ratio(self):
        pygame.init()
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        width_ratio = screen_width / 2048
        height_ratio = screen_height / 1152
        return width_ratio, height_ratio    
    
    
    def play(self):
        pygame.init()
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Menu")
        width_ratio,height_ratio=self.ratio()
        background = pygame.image.load('constellation.jpeg')
        background = pygame.transform.scale(background, (screen_width, screen_height))
        running = True
        screen.blit(background, (0, 0))
        square_size = 50*width_ratio
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    from menu_staryinsh import menu
                    menu()
                
                self.hit_box(event, square_size, screen,width_ratio, height_ratio)
                    
                pygame.display.flip()
                
                if self.align_condition():
                    self.show_board()
                if self.nb_pieces_full_placed == 15:
                    self.show_board()   
                    running = False
        pygame.quit()


def launch_game():
    game = Game()
    game.play()

launch_game()