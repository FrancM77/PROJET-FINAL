import pygame
from pygame.locals import *
from display import Display
from piece import Piece
from align import Align


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
    
    
    
    #function for pawn management
    def piece_action(self, x, y, event, square_size, screen, i, j):
        if self.multialign:
            self.align.alignment_choice(i,j,x,y,event,square_size,screen)
            return True
        if self.remove_mode:
            self.piece.remove_piece(x, y, event, square_size, screen, i, j)
            return True
        if self.nb_pieces_placed_depart < 2:
            return self.piece.place_first_piece(x, y, event, square_size, screen, i, j)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.piece.place_third_piece(x, y, event, square_size, screen, i, j)
                if self.placed_third_piece and not self.align.align_condition(screen):
                    self.change_player()
                    self.placed_second_piece = False
                    self.previous_position = None   
                    return
                else:
                    return
            else:
                self.placed_second_piece, self.previous_position = self.piece.place_second_piece(x, y,event, square_size, screen, i, j)
        return False
    #end of function for pawn management
    
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
        
        self.display = Display(self,self.width_ratio,self.height_ratio,self.piece_image)
        self.piece= Piece(self,self.width_ratio,self.height_ratio,self.piece_image)
        self.align = Align(self,self.width_ratio,self.height_ratio,self.piece_image)
        if self.type == "AI":
            from game_ia import AI
            ai = AI(self,self.piece,self.display,self.align,self.width_ratio,self.height_ratio,self.piece_image)
        
        self.display.display_piece(screen)
        self.play_music("game")
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
                self.align.align_condition(screen)
                pygame.display.flip()
                
                self.display.display_info(screen,space_font)
                
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
    
launch_game("blitz","AI")