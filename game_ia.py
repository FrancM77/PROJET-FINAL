import pygame
import random

class AI:
    def __init__(self, game,piece, display,align, width_ratio, height_ratio, piece_image):
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
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 2:
                self.game.board[j][i] = 6
                self.display.display_piece(screen)
                pygame.display.flip()
                return True, (i, j)

    def place_third_piece(self, screen):
        previous_i, previous_j = self.previous_position
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.piece.is_valid_move(previous_i, previous_j, i, j) and self.game.board[j][i] == 0 and self.game.board[j][i] != 'N': 
                self.piece.flip_pieces(previous_i, previous_j, i, j)
                pygame.time.delay(500)
                self.game.board[j][i] = 2
                self.game.board[previous_j][previous_i] = 4
                self.display.display_piece(screen)
                self.game.change_player()
                pygame.display.flip()
                return True
    
    
    def remove_piece(self, screen):
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

    def play(self, screen):
        if self.game.remove_mode:
            self.remove_piece(screen)
            return 
        if self.game.nb_pieces_placed_depart < 2:
            return self.place_first_piece(screen)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.place_third_piece(screen)
                if self.placed_third_piece:
                    self.previous_position = None
                    self.placed_second_piece = False
            else:
                self.placed_second_piece, self.previous_position = self.place_second_piece(screen)
        return False