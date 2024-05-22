import pygame
import random


class AI:
    def __init__(self, game):
        self.game = game
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
        self.game.display_piece(screen)
        self.game.change_player()
        pygame.display.flip()

    def place_second_piece(self, screen):
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 2:
                self.game.board[j][i] = 6
                self.game.display_piece(screen)
                pygame.display.flip()
                return True, (i, j)

    def place_third_piece(self, screen):
        previous_i, previous_j = self.previous_position
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.is_valid_move(previous_i, previous_j, i, j) and self.game.board[j][i] == 0 and self.game.board[j][i] != 'N': 
                self.game.flip_pieces(previous_i, previous_j, i, j)
                pygame.time.delay(500)
                self.game.board[j][i] = 2
                self.game.board[previous_j][previous_i] = 4
                self.game.display_piece(screen)
                if self.game.align_condition(screen):
                    self.game.change_player()
                pygame.display.flip()
                return True
            
            
    def remove_piece(self, screen):
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 2:
                pygame.time.delay(500)
                self.game.board[j][i] = 0
                self.game.display_piece(screen)
                self.game.update_points()
                self.game.display_points(screen)
                self.game.remove_mode = False
                pygame.display.flip()
                return True
            
    def alignment_choice(self,screen):
        while True:
            random_choice = random.choice(self.game.alignments)
            coor = random.choice(random_choice)
            for alignment in self.game.alignments:
                if coor in alignment:
                    self.game.remove_alignment(screen, alignment)
                    self.game.multialign = False
                    return True

    def play(self, screen):
        if self.game.multialign:
            self.alignment_choice(screen)
            return True
        if self.game.remove_mode:
            self.remove_piece(screen)
            return 
        elif self.game.nb_pieces_placed_depart < 2:
            return self.place_first_piece(screen)
        else:
            if self.placed_second_piece:
                self.placed_third_piece = self.place_third_piece(screen)
                if self.placed_third_piece and not self.game.align_condition(screen):
                    self.game.change_player()
                    self.placed_second_piece = False
                    self.previous_position = None   
                    return
                else:
                    return
            else:
                self.placed_second_piece, self.previous_position = self.place_second_piece(screen)
        return False