import pygame
import random

class AI:
    '''
    This class represents the AI player.
    '''
    def __init__(self, game,piece, display,align, width_ratio, height_ratio, piece_image):
        '''
        This function initializes the AI player.
        
        params:
        game: the game object , type: Game
        display: the display object , type: Display
        align: the align object , type: Align
        piece: the piece object , type: Piece
        width_ratio: the width ratio , type: float
        height_ratio: the height ratio , type: float
        piece_image: the image of the piece , type: pygame.Surface
        '''
        self.game = game
        self.display = display
        self.align = align
        self.piece = piece
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.piece_image = piece_image
        self.placed_second_piece = False
        self.placed_third_piece = False
        self.previous_position = None

    def place_first_piece(self, screen):
        '''
        This function places the first piece of the AI player.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        '''
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 0:
                break
        self.game.board[j][i] = 2
        self.game.nb_pieces_placed_depart += 1
        self.display.display_piece(screen)
        self.game.change_player()
        pygame.display.flip()

    def place_second_piece(self, screen):
        '''
        This function places the second piece of the AI player.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        
        return:
        True if the AI player has placed the second piece with the coordinates of the placement
        '''
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 2:
                self.game.board[j][i] = 6
                self.display.display_piece(screen)
                pygame.display.flip()
                return True, (i, j)

    def place_third_piece(self, screen):
        '''
        This function places the third piece of the AI player.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        '''
        previous_i, previous_j = self.previous_position
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.piece.is_valid_move(previous_i, previous_j, i, j) and self.game.board[j][i] == 0 and self.game.board[j][i] != 'N': 
                self.piece.flip_pieces(previous_i, previous_j, i, j)
                pygame.time.delay(500)
                self.game.board[j][i] = 2
                self.game.board[previous_j][previous_i] = 4
                self.display.display_piece(screen)
                if self.align.align_condition(screen):
                    self.game.change_player()
                pygame.display.flip()
                return True
            
            
    def remove_piece(self, screen):
        '''
        This function removes a piece from the board.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        '''
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 2:
                pygame.time.delay(500)
                self.game.board[j][i] = 0
                self.display.display_piece(screen)
                self.game.update_points()
                self.display.display_points(screen)
                self.game.remove_mode = False
                pygame.display.flip()
                return True
            
    def alignment_choice(self,screen):
        '''
        This function removes an alignment from the board.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        
        return:
        True if the AI player has removed an alignment
        '''
        while True:
            random_choice = random.choice(self.game.alignments)
            coor = random.choice(random_choice)
            for alignment in self.game.alignments:
                if coor in alignment:
                    self.align.remove_alignment(screen, alignment)
                    self.game.multialign = False
                    return True

    def play(self, screen):
        '''
        This function plays the AI player.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        
        return:
        True if the AI player has played, False otherwise
        '''
        if self.game.multialign:
            self.alignment_choice(screen)
            return True
        if self.game.remove_mode:
            self.remove_piece(screen)
            return 
        elif self.game.nb_pieces_placed_depart < 10:
            return self.place_first_piece(screen)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.place_third_piece(screen)
                if self.placed_third_piece and not self.align.align_condition(screen):
                    self.game.change_player()
                    self.placed_second_piece = False
                    self.previous_position = None   
                    return
                else:
                    return
            else:
                self.placed_second_piece, self.previous_position = self.place_second_piece(screen)
        return False