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
        self.multialign= False
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
        self.player = 2 if self.player == 1 else 1
        
    
    def update_points(self):
        if self.player == 1:
            self.player_1_points += 1
        else:
            self.player_2_points += 1
        self.change_player()
        

    #apply offset to the pieces
    def recover_offset(self,j):
        count = 0
        for row in range(11):
            if self.board[j][row] == 'N':
                count += 1
            elif self.board[j][row] in [0,1, 2, 3, 4, 5, 6]:
                return count
    
    #function to place pieces on the board
    
    def place_first_piece(self, x, y, event, square_size, screen, i, j):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            if self.board[j][i] == 0:
                self.nb_pieces_placed_depart += 1
                self.board[j][i] = 1 if self.player == 1 else 2
                self.display_piece(screen)
                self.change_player()
                self.play_sound_once("first_piece")
        return False
    
    
    def place_second_piece(self, x, y, event, square_size, screen, i, j):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            player = self.player
            i += self.recover_offset(j)
            if self.player == player and self.board[j][i] == player:
                self.board[j][i] = player + 4
                self.display_piece(screen)
                self.play_sound_once("second_piece")
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
                self.play_sound_once("third_piece")
                return True
        return False
    
    #end of function to place pieces on the board
    
    #function for pawn management
    def piece_action(self, x, y, event, square_size, screen, i, j):
        if self.multialign:
            self.alignment_choice(i,j,x,y,event,square_size,screen)
            return True
        if self.remove_mode:
            self.remove_piece(x, y, event, square_size, screen, i, j)
            return True
        if self.nb_pieces_placed_depart < 10:
            return self.place_first_piece(x, y, event, square_size, screen, i, j)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.place_third_piece(x, y, event, square_size, screen, i, j)
                if self.placed_third_piece and not self.align_condition(screen):
                    self.change_player()
                    self.placed_second_piece = False
                    self.previous_position = None   
                    return
                else:
                    return
            else:
                self.placed_second_piece, self.previous_position = self.place_second_piece(x, y,event, square_size, screen, i, j)
        return False
    #end of function for pawn management

    #function to remove a piece
    def remove_piece(self, x, y, event, square_size, screen, i, j):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
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
    #end of function to remove a piece
    
    #function to verify if the move is valid
    
    def verify_move_column(self, start_x, start_y, end_y,value):
        for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
            if self.board[y][start_x] in [1, 2]:
                return False
            if self.board[y][start_x] in [3, 4]:
                for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                    if self.board[y][start_x] == 0 and self.board[y+value][start_x] in [3, 4] :
                        return False
        return True
    
    def verify_move_line(self, start_x, start_y, end_x,value):
        for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
            if self.board[start_y][x] in [1, 2]:
                return False
            if self.board[start_y][x] in [3, 4]:
                for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                    if self.board[start_y][x] == 0 and self.board[start_y][x+value] in [3, 4]:
                        return False
        return True
    
    def verify_move_diagonal(self, start_x, start_y, end_x, end_y, value):
        for x, y in zip(range(min(start_x, end_x) + 1, max(start_x, end_x)), range(min(start_y, end_y) + 1, max(start_y, end_y))):
                if self.board[y][x] in [1, 2]:
                    return False
                if self.board[y][x] in [3, 4]:
                    for x, y in zip(range(min(start_x, end_x) + 1, max(start_x, end_x)), range(min(start_y, end_y) + 1, max(start_y, end_y))):
                        if self.board[y][x] == 0 and self.board[y+value][x+value] in [3, 4]:
                            return False
        return True
        
        
    def is_valid_move(self, start_x, start_y, end_x, end_y):
        # column (|)
        if start_x == end_x:  
            if start_y < end_y:
                return self.verify_move_column(start_x, start_y, end_y,-1)
            if start_y > end_y:
                return self.verify_move_column(start_x, start_y, end_y,1)
        # line (-)    
        elif start_y == end_y:  
            if start_x < end_x:
                return self.verify_move_line(start_x, start_y, end_x,-1)
            if start_x > end_x:
                return self.verify_move_line(start_x, start_y, end_x,1)
        # Diagonal (\)
        elif start_x - end_x == start_y - end_y:  
            if start_x < end_x:
                return self.verify_move_diagonal(start_x, start_y, end_x, end_y,-1)
            if start_x > end_x:
                return self.verify_move_diagonal(start_x, start_y, end_x, end_y,1)
        else:
            return False
        
    #end of function to verify if the move is valid
    
    #functions to flip the pieces

    def flip_pieces(self, start_x, start_y, end_x, end_y):
        # column (|)
        if start_x == end_x:  
            for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                self.flip(y, start_x)
        # line (-)
        elif start_y == end_y:  
            for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                self.flip(start_y, x)
        # Diagonal (\)
        elif start_x - end_x == start_y - end_y:  
            for i in range(1, abs(start_x - end_x)):
                x = min(start_x, end_x) + i
                y = min(start_y, end_y) + i
                self.flip(y, x) 
        
    def flip(self,a,b):
        if self.board[a][b] == 3:
            self.board[a][b] = 4
        elif self.board[a][b] == 4:
            self.board[a][b] = 3
    
    #end of functions to flip the pieces
    
    #function to check if there is an alignment
    def align_check(self,start_x, start_y, x, y):
        for j in range(5):
            if self.board[start_y + j * y][start_x + j * x] != self.board[start_y][start_x]:
                return False
        return True
    
    def align_condition(self, screen):
        self.alignments = []
        for j in range(11):
            for i in range(11):
                if self.board[j][i] in [3, 4]:  
                    player_owner = 2 if self.board[j][i] == 4 else 1
                    # line (-)
                    if i <= 6 and self.align_check(i, j, 1, 0):
                        if player_owner == self.player:
                            alignment = [(j, i + k) for k in range(5)]
                            self.alignments.append(alignment)
                    
                    # column (|)
                    if j <= 6 and self.align_check(i, j, 0, 1):
                        if player_owner == self.player:
                            alignment = [(j + k, i) for k in range(5)]
                            self.alignments.append(alignment)
                    
                    # Diagonal (\)
                    if j <= 6 and i <= 6 and self.align_check(i, j, 1, 1):
                        if player_owner == self.player:
                            alignment = [(j + k, i + k) for k in range(5)]
                            self.alignments.append(alignment)
        if len(self.alignments) == 1:
            self.remove_alignment(screen, self.alignments[0])
            return True
        elif len(self.alignments) > 1:
            self.multialign = True
            return True
        return False
    #end of function to check if there is an alignment
    
    #function to remove alignment
    def alignment_choice(self,i,j,x,y,event,square_size,screen):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.recover_offset(j)
            for alignment in self.alignments:
                if (j,i) in alignment:
                    self.remove_alignment(screen, alignment)
                    self.multialign = False
                    break
        return False

    def remove_alignment(self, screen, alignment):
        for (j, i) in alignment:
            self.board[j][i] = 0
        self.display_piece(screen)
        self.remove_mode = True
        self.play_sound_once("alignement")
    #end of function to remove alignment

    #functions to display the pieces on the board
    def display_piece(self, screen):
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
        
        for j, (start, end, y_offset) in enumerate(piece_data):
            for i in range(start, end):
                self.display_piece_action((649 + (i * 75) - 31) * self.width_ratio, (y_offset - (i * 43) - 35) * self.height_ratio, screen, i, j)

    
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
    #end of functions to display the pieces on the board
            
    
    # function which takes care of the pieces on the sides to count the points
    
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
            
    # end of function which takes care of the pieces on the sides to count the points
    
    #function to load the background
    def load_background(self, screen):
        background = pygame.image.load('images/board.jpeg')
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.blit(background, (0, 0))     
    #end of function to load the background

    #function to manage the pieces on the board
    def hit_box(self, event, square_size, screen):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            positions = [
                (4, 697, 190, 75, -43),  
                (7, 622, 320, 75, -43),  
                (8, 622, 405, 75, -43),  
                (9, 647, 495, 75, -43),  
                (10, 622, 580, 75, -43), 
                (9, 697, 625, 75, -43),  
                (10, 697, 712, 75, -43), 
                (9, 773, 755, 75, -43),  
                (8, 848, 800, 75, -43),  
                (7, 925, 842, 75, -43),  
                (4, 1075, 843, 75, -43) 
            ]

            for j, (count, base_x, base_y, x_step, y_step) in enumerate(positions):
                for i in range(count):
                    x = (base_x + i * x_step) * self.width_ratio
                    y = (base_y + i * y_step) * self.height_ratio
                    self.piece_action(x, y, event, square_size, screen, i, j)

    #end of function to manage the pieces on the board

    #function to verify if the player has won
    def victory_condition(self):         
        if self.player_1_points == self.nb_circle:
            return True,1
        if self.player_2_points == self.nb_circle:
            return True,2
        return False,None
    #end of function to verify if the player has won

    #function to display the information on the screen
    def display_info(self, screen, font):
        RGB = (235,117,141) if self.player == 1 else (84, 181, 97)
        while self.nb_pieces_placed_depart < 10:
            if self.type == "AI":
                text = font.render(f"Veuillez placer un de vos 5 pions", True, RGB)
                screen.blit(text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                text = font.render(f"Joueur {self.player}, veuillez placer un de vos 5 pions", True, RGB)
                screen.blit(text, (550*self.width_ratio, 900*self.height_ratio))
            return
        if self.multialign:
            if self.type == "AI":
                multialign_text = font.render(f"Veuillez supprimer un de vos alignements", True, RGB)
                screen.blit(multialign_text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                multialign_text = font.render(f"Joueur {self.player}, veuillez supprimer un de vos alignements", True, RGB)
                screen.blit(multialign_text, (470*self.width_ratio, 900*self.height_ratio))
            return
        elif self.remove_mode:
            if self.type == "AI":
                remove_text = font.render(f"Veuillez supprimer un de vos pions", True, RGB)
                screen.blit(remove_text, (650*self.width_ratio, 900*self.height_ratio))
            else:
                remove_text = font.render(f"Joueur {self.player}, veuillez supprimer un de vos pions", True, RGB)
                screen.blit(remove_text, (550*self.width_ratio, 900*self.height_ratio))
            return 
        elif self.type == "AI":
            player_text = font.render(f"C'est à votre tour", True, RGB)
            screen.blit(player_text, (800*self.width_ratio, 900*self.height_ratio)) 
        else:
            player_text = font.render(f"C'est au tour du joueur {self.player}", True, RGB)
            screen.blit(player_text, (750*self.width_ratio, 900*self.height_ratio)) 
    #end of function to display the information on the screen
    
    #functions to play music and sound
    def play_music(self,title):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f'sounds/{title}.mp3')
        pygame.mixer.music.play(-1)
        
    def play_sound_once(self,title):
        sound = pygame.mixer.Sound(f'sounds/{title}.mp3')
        sound.play()
    #end of functions to play music and sound
    
    
    #function to play the game
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
                self.align_condition(screen)
                pygame.display.flip()
                
                self.display_info(screen,space_font)
                
                if self.victory_condition()[0]:
                    self.play_music("game_over")  
                    from victory_screen import victory_screen
                    victory_screen(self.victory_condition()[1],self.mode,self.type)
                    running = False
        pygame.quit()
    #end of function to play the game

def launch_game(mode,type_game):
    game = Game(mode,type_game)
    game.play()
    
launch_game("normal","AI")