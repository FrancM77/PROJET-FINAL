import pygame
from pygame.locals import *

class Game:
    def __init__(self,mode,type_game):
        self.board= [['N', 0, 0 ,0 ,0, 'N', 'N' ,'N', 'N' ,'N', 'N'],
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
        
        self.mode = mode
        self.type = type_game
        self.player = 1
        self.nb_pieces_placed_depart = 0
        self.player_1_points = 0 
        self.player_2_points = 0
        self.remove_mode = False
        self.placed_second_piece = False
        self.placed_third_piece = False
        if self.mode == "normal":
            self.nb_circle = 3
        elif self.mode == "blitz":
            self.nb_circle = 1   
    
    def load_pieces(self):
        self.piece_image = {}
        for i in range(1,7):
            self.piece_image[i] = pygame.image.load(f'./pion/pion{i}.png')
            self.piece_image[i] = pygame.transform.scale(self.piece_image[i], (60*self.height_ratio, 60*self.width_ratio))

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
        return False, None

   

    def place_third_piece(self, x, y, event, square_size, screen, i, j):
        previous_i , previous_j = self.previous_position
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            if self.is_valid_move(previous_i, previous_j, i, j) and self.board[j][i] == 0:
                self.flip_pieces(previous_i, previous_j, i, j)
                self.board[j][i] = 1 if self.player == 1 else 2
                self.board[previous_j][previous_i] = 3 if self.player == 1 else 4
                self.display_piece(screen)
                self.change_player()
                return True
        return False
    
    

    def is_valid_move(self, start_x, start_y, end_x, end_y):
        if start_x == end_x:  # colonne (|)
            # Vérifier les pions en chemin
            for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                if self.board[y][start_x] in [1, 2]:  # Pions 1 et 2
                    return False
            return True
        elif start_y == end_y:  # ligne (-)
            # Vérifier les pions en chemin
            for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                if self.board[start_y][x] in [1, 2]:  # Pions 1 et 2
                    return False
            return True
        elif start_x - end_x == start_y - end_y:  # Diagonal utile (\)
            # Vérifier les pions en chemin
            min_x = min(start_x, end_x)
            max_x = max(start_x, end_x)
            min_y = min(start_y, end_y)
            max_y = max(start_y, end_y)
            for i in range(1, abs(start_x - end_x)):
                x = min_x + i
                y = min_y + i
                if self.board[y][x] in [1, 2]:  # Pions 1 et 2
                    return False
            return True
        else:
            return False

    def flip_pieces(self, start_x, start_y, end_x, end_y):
        if start_x == end_x:  # colonne (|)
            # Retourner les pions
            for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                if self.board[y][start_x] == 3:
                    self.board[y][start_x] = 4  # Retournement du pion 3 en pion 4
                elif self.board[y][start_x] == 4:
                    self.board[y][start_x] = 3  # Retournement du pion 4 en pion 3

        elif start_y == end_y:  # ligne (-)
            # Retourner les pions
            for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                if self.board[start_y][x] == 3:
                    self.board[start_y][x] = 4  # Retournement du pion 3 en pion 4
                elif self.board[start_y][x] == 4:
                    self.board[start_y][x] = 3  # Retournement du pion 4 en pion 3

        elif start_x - end_x == start_y - end_y:  # Diagonal utile (\)
            # Retourner les pions
            min_x = min(start_x, end_x)
            max_x = max(start_x, end_x)
            min_y = min(start_y, end_y)
            max_y = max(start_y, end_y)
            for i in range(1, abs(start_x - end_x)):
                x = min_x + i
                y = min_y + i
                if self.board[y][x] == 3:
                    self.board[y][x] = 4  # Retournement du pion 3 en pion 4
                elif self.board[y][x] == 4:
                    self.board[y][x] = 3  # Retournement du pion 4 en pion 3


    def align_check(self,start_x, start_y, x, y):
            for j in range(5):
                if self.board[start_y + j * y][start_x + j * x] != self.board[start_y][start_x]:
                    return False
            return True
        
    def align_condition(self, screen):
        for j in range(11):
            for i in range(11):
                if self.board[j][i] in [3, 4]:
                    # Horizontal (-)
                    if i <= 6 and self.align_check(i, j, 1, 0):
                        for k in range(5):
                            self.board[j][i + k] = 0
                            self.display_piece(screen)
                        self.change_player()
                        self.remove_mode = True
                        self.play_sound_once("alignement")
                        return True
                    # Vertical (|)
                    if j <= 6 and self.align_check(i, j, 0, 1):
                        for k in range(5):
                            self.board[j + k][i] = 0
                            self.display_piece(screen)
                        self.change_player()
                        self.remove_mode = True
                        self.play_sound_once("alignement")
                        return True
                    # Diagonal utile (\)
                    if j <= 6 and i <= 6 and self.align_check(i, j, 1, 1):
                        for k in range(5):
                            self.board[j + k][i + k] = 0
                            self.display_piece(screen)
                        self.change_player()
                        self.remove_mode = True
                        self.play_sound_once("alignement")
                        return True
        return False

    def update_points(self):
        if self.player == 1:
            self.player_1_points += 1
        else:
            self.player_2_points += 1
        self.change_player()



    def piece_action(self, x, y, event, square_size, screen, i, j):
        if self.remove_mode:
            self.remove_piece(x, y, event, square_size, screen, i, j)
            return False
        if self.nb_pieces_placed_depart < 6:
            return self.place_first_piece(x, y, event, square_size, screen, i, j)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.place_third_piece(x, y, event, square_size, screen, i, j)
                if self.placed_third_piece:
                    self.placed_second_piece = False
                    self.previous_position = None   
            else:
                self.placed_second_piece, self.previous_position = self.place_second_piece(x, y,event, square_size, screen, i, j)

        return False


    def remove_piece(self, x, y, event, square_size, screen, i, j):
        if self.remove_mode and x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            if self.board[j][i] == self.player:
                self.board[j][i] = 0
                self.display_piece(screen)
                self.update_points()
                self.display_points(screen)
                self.remove_mode = False
                self.placed_second_piece = False
                self.placed_third_piece = False
                self.previous_position = None
                return True
        return False


    def display_piece(self,screen):
        self.load_background(screen)
        for i in range(1,5):
            j=0
            self.display_piece_action((649+(i*75)-31)*self.width_ratio, (265-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(7):
            j=1
            self.display_piece_action((649+(i*75)-31)*self.width_ratio, (345-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(8):
            j=2
            self.display_piece_action((649+(i*75)-31)*self.width_ratio, (435-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(9):
            j=3
            self.display_piece_action((647+(i*75)-31)*self.width_ratio, (520-(i*43)-35)*self.height_ratio,screen,i,j)    
        for i in range(10):
            j=4
            self.display_piece_action((647+(i*75)-31)*self.width_ratio, (605-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(1,10):
            j=5
            self.display_piece_action((649+(i*75)-31)*self.width_ratio, (695-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(1,11): 
            j=6
            self.display_piece_action((649+(i*75)-31)*self.width_ratio, (782-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(2,11):
            j=7
            self.display_piece_action((649+(i*75)-31)*self.width_ratio, (870-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(3,11):
            j=8
            self.display_piece_action((650+(i*75)-31)*self.width_ratio, (957-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(4,11):
            j=9
            self.display_piece_action((650+(i*75)-31)*self.width_ratio, (1043-(i*43)-35)*self.height_ratio,screen,i,j)
        for i in range(5,11):
            j=10
            self.display_piece_action((650+(i*75)-31)*self.width_ratio, (1130-(i*43)-35)*self.height_ratio,screen,i,j)
    
    def load_background(self, screen):
        background = pygame.image.load('images/board.jpeg')
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.blit(background, (0, 0))     
            
    
    # fonction qui s'occupe des pieces sur les cotes pour compter les points
    
    def load_side_img(self,number,alpha,x,y,screen):
        image = self.piece_image[number].convert_alpha()
        image.set_alpha(alpha)
        image = pygame.transform.scale(image, (100*self.width_ratio, 100*self.height_ratio))
        screen.blit(image, (x*self.width_ratio, y*self.height_ratio))
        return image
    
    def display_points(self, screen):
        for i in range(self.player_1_points):
            self.load_side_img(1,256,10,(10+(i*95)),screen)
        for i in range(self.player_2_points):
            self.load_side_img(2,256,1940,(1050-(i*95)),screen)
                    
    def display_side_piece_start(self,screen):
        for i in range(self.nb_circle):
            self.load_side_img(1,2,10,(10+(i*95)),screen)
            self.load_side_img(2,3,1940,(1050-(i*95)),screen)
            
    # fin de gestion des pieces sur les cotes
    
    
    def display_piece_action(self, x2, y2, screen, i, j):
        self.display_side_piece_start(screen)
        self.display_points(screen)
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



    def hit_box(self, event, square_size, screen):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(4):
                    j = 0
                    x,y = (697 + (i * 75))*self.width_ratio, (190 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(7):
                    j = 1
                    x,y = (622 + (i * 75))*self.width_ratio, (320 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(8):
                    j = 2
                    x,y = (622 + (i * 75))*self.width_ratio, (405 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(9):
                    j = 3
                    x,y = (647 + (i * 75))*self.width_ratio, (495 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(10):
                    j = 4
                    x,y = (622 + (i * 75))*self.width_ratio, (580 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(9):
                    j = 5
                    x,y = (697 + (i * 75))*self.width_ratio, (625 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(10):
                    j = 6
                    x,y = (697 + (i * 75))*self.width_ratio, (712 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(9):
                    j = 7
                    x,y = (773 + (i * 75))*self.width_ratio, (755 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(8):
                    j = 8
                    x,y = (848 + (i * 75))*self.width_ratio, (800 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(7):
                    j = 9
                    x,y = (925 + (i * 75))*self.width_ratio, (842 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)
                for i in range(4):
                    j = 10
                    x,y = (1075 + (i * 75))*self.width_ratio, (843 - (i * 43))*self.height_ratio
                    self.piece_action(x,y,event, square_size, screen,i,j)


    def victory_condition(self):         
        if self.player_1_points == self.nb_circle:
            return True,1
        if self.player_2_points == self.nb_circle:
            return True,2
        return False,None
    
    
        
    def show_board(self):
        for i in range(11):
            for j in range(10):
                print(self.board[i][j], end=" ")
            print()

    
    
    def display_info(self, screen, font):
        RGB = (235,117,141) if self.player == 1 else (84, 181, 97)
        while self.nb_pieces_placed_depart < 6:
            if self.type == "AI":
                text = font.render(f"Veuillez placer un de vos 5 pions", True, RGB)
                screen.blit(text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                text = font.render(f"Joueur {self.player}, veuillez placer un de vos 5 pions", True, RGB)
                screen.blit(text, (550*self.width_ratio, 900*self.height_ratio))
            
            return
        if self.remove_mode:
            if self.type == "AI":
                remove_text = font.render(f"Veuillez supprimer un de vos pions", True, RGB)
                screen.blit(remove_text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                remove_text = font.render(f"Joueur {self.player}, veuillez supprimer un de vos pions", True, RGB)
                screen.blit(remove_text, (550*self.width_ratio, 900*self.height_ratio))
            return 
        if self.type == "AI":
            player_text = font.render(f"C'est à votre tour", True, RGB)
            screen.blit(player_text, (800*self.width_ratio, 900*self.height_ratio)) 
        else:
            player_text = font.render(f"C'est au tour du joueur {self.player}", True, RGB)
            screen.blit(player_text, (750*self.width_ratio, 900*self.height_ratio)) 

    def play_music(self,title):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f'sounds/{title}.mp3')
        pygame.mixer.music.play(-1)
        
    def play_sound_once(self,title):
        sound = pygame.mixer.Sound(f'sounds/{title}.mp3')
        sound.play()
    
    def play(self):
        pygame.init()
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Staryinsh")
        self.width_ratio = screen_width / 2048
        self.height_ratio = screen_height / 1152
        background = pygame.image.load('images/board.jpeg')
        background = pygame.transform.scale(background, (screen_width, screen_height))
        running = True
        screen.blit(background, (0, 0))
        square_size = 50*self.width_ratio
        space_font= pygame.font.Font("./font/SpaceMono-Bold.ttf", 36)
        self.load_pieces()
        self.display_piece(screen)
        self.play_music("game")
        if self.type == "AI":
            from game_ia import AI
            ai = AI(self)
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.play_music("menu")
                    from staryinsh_home import menu
                    menu()
                if self.player == 2 and self.type == "AI":
                        ai.play(screen)
                else:
                    self.hit_box(event, square_size, screen)
                
                pygame.display.flip()
                self.align_condition(screen)
                self.display_info(screen,space_font)
                if self.victory_condition()[0]:
                    print(f"le joueur {self.victory_condition()[1]} a gagné")
                    self.play_music("game_over")  
                    from victory_screen import victory_screen
                    victory_screen(self.victory_condition()[1],self.mode,self.type)
                    running = False
        pygame.quit()


def launch_game(mode,type_game):
    game = Game(mode,type_game)
    game.play()

