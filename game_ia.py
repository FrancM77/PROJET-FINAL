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
            j, i = random.randint(0, 10), random.randint(0, 10)
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
        if self.previous_position is None:
            return
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.is_valid_move(self.previous_position[0], self.previous_position[1], i, j):
                if self.game.board[j][i] == 0 and self.game.board[j][i] != 'N':
                    pygame.time.delay(500)
                    self.game.board[j][i] = 2
                    self.game.board[self.previous_position[1]][self.previous_position[0]] = 4
                    self.game.display_piece(screen)
                    self.game.change_player()
                    pygame.display.flip()
                    return True

    def remove_piece(self, screen):
        while True:
            i, j = random.randint(0, 10), random.randint(0, 10)
            if self.game.board[j][i] == 2:
                self.game.board[j][i] = 0
                self.game.display_piece(screen)
                self.game.update_points()
                self.game.display_points(screen)
                self.game.remove_mode = False
                pygame.display.flip()
                return True

    def play(self, screen):
        if self.game.remove_mode:
            self.remove_piece(screen)
            return 
        if self.game.nb_pieces_placed_depart < 6:
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