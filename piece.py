from display import Display


class Piece:
    '''
    This class is used to place the pieces on the board and to remove them.
    '''
    def __init__(self,game,width_ratio,height_ratio,piece_image):
        '''
        This function initializes the Piece class.
        
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
        self.display = Display(game,self.width_ratio,self.height_ratio,self.piece_image)
    
    
    def place_first_piece(self, x, y, event, square_size, screen, i, j):
        '''
        This function places the first piece on the board.
        
        params:
        x: the x-coordinate , type: int
        y: the y-coordinate , type: int
        event: the event , type: pygame.event
        square_size: the size of the square , type: int
        screen: the screen to display the piece on , type: pygame.Surface
        i: the i-coordinate , type: int
        j: the j-coordinate , type: int
        
        return:
        True if the piece is placed else False , type: bool
        '''
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.game.recover_offset(j)
            if self.game.board[j][i] == 0:
                self.game.nb_pieces_placed_depart += 1
                self.game.board[j][i] = 1 if self.game.player == 1 else 2
                self.display.display_piece(screen)
                self.game.change_player()
                self.game.play_sound_once("first_piece")
                return True
        return False
    
    
    def place_second_piece(self, x, y, event, square_size, screen, i, j):
        '''
        This function places the second piece on the board.
        
        params:
        x: the x-coordinate , type: int
        y: the y-coordinate , type: int
        event: the event , type: pygame.event
        square_size: the size of the square , type: int
        screen: the screen to display the piece on , type: pygame.Surface
        i: the i-coordinate , type: int
        j: the j-coordinate , type: int
        
        return:
        True if the piece is placed with the coordinates else False with coordinates None , type: bool, tuple
        '''
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            player = self.game.player
            i += self.game.recover_offset(j)
            if self.game.player == player and self.game.board[j][i] == player:
                self.game.board[j][i] = player + 4
                self.display.display_piece(screen)
                self.game.play_sound_once("second_piece")
                return True, (i, j)
        return False, None

   
    def place_third_piece(self, x, y, event, square_size, screen, i, j):
        '''
        This function places the third piece on the board.
        
        params:
        x: the x-coordinate , type: int
        y: the y-coordinate , type: int
        event: the event , type: pygame.event
        square_size: the size of the square , type: int
        screen: the screen to display the piece on , type: pygame.Surface
        i: the i-coordinate , type: int
        j: the j-coordinate , type: int
        
        return:
        True if the piece is placed else False , type: bool
        '''
        previous_i , previous_j = self.game.previous_position
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.game.recover_offset(j)
            if self.is_valid_move(previous_i, previous_j, i, j) and self.game.board[j][i] == 0:
                self.flip_pieces(previous_i, previous_j, i, j)
                self.game.board[j][i] = 1 if self.game.player == 1 else 2
                self.game.board[previous_j][previous_i] = 3 if self.game.player == 1 else 4
                self.display.display_piece(screen)
                self.game.play_sound_once("third_piece")
                return True
        return False
    
    
    def remove_piece(self, x, y, event, square_size, screen, i, j):
        '''
        This function removes a piece from the board.
        
        params:
        x: the x-coordinate , type: int
        y: the y-coordinate , type: int
        event: the event , type: pygame.event
        square_size: the size of the square , type: int 
        screen: the screen to display the piece on , type: pygame.Surface
        i: the i-coordinate , type: int
        j: the j-coordinate , type: int
        
        return:
        True if the piece is removed else False , type: bool
        '''
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.game.recover_offset(j)
            if self.game.board[j][i] == self.game.player:
                self.game.board[j][i] = 0
                self.display.display_piece(screen)
                self.game.update_points()
                self.display.display_points(screen)
                self.game.remove_mode = False
                self.game.placed_second_piece = False
                self.game.placed_third_piece = False
                self.game.previous_position = None
                return True
        return False
    
    
    def verify_move_column(self, start_x, start_y, end_y,value):
        '''
        This function verifies if the move is valid in the column we need (|).
        
        params:
        start_x: the x-coordinate of the start , type: int
        start_y: the y-coordinate of the start , type: int
        end_y: the y-coordinate of the end , type: int
        value: the value to add to the y-coordinate , type: int
        
        return:
        True if the move is valid else False , type: bool
        '''
        for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
            if self.game.board[y][start_x] in [1, 2]:
                return False
            if self.game.board[y][start_x] in [3, 4]:
                for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                    if self.game.board[y][start_x] == 0 and self.game.board[y+value][start_x] in [3, 4] :
                        return False
        return True
    
    
    def verify_move_line(self, start_x, start_y, end_x,value):
        '''
        This function verifies if the move is valid in the line we need (-).
        
        params:
        start_x: the x-coordinate of the start , type: int
        start_y: the y-coordinate of the start , type: int
        end_x: the x-coordinate of the end , type: int
        value: the value to add to the x-coordinate , type: int
        
        return:
        True if the move is valid else False , type: bool
        '''
        for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
            if self.game.board[start_y][x] in [1, 2]:
                return False
            if self.game.board[start_y][x] in [3, 4]:
                for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                    if self.game.board[start_y][x] == 0 and self.game.board[start_y][x+value] in [3, 4]:
                        return False
        return True
    
    
    def verify_move_diagonal(self, start_x, start_y, end_x, end_y, value):
        '''
        This function verifies if the move is valid in the diagonal we need (\).
        
        params:
        start_x: the x-coordinate of the start , type: int
        start_y: the y-coordinate of the start , type: int
        end_x: the x-coordinate of the end , type: int
        end_y: the y-coordinate of the end , type: int
        value: the value to add to the x-coordinate and y-coordinate , type: int
        
        return:
        True if the move is valid else False , type: bool
        '''
        for x, y in zip(range(min(start_x, end_x) + 1, max(start_x, end_x)), range(min(start_y, end_y) + 1, max(start_y, end_y))):
                if self.game.board[y][x] in [1, 2]:
                    return False
                if self.game.board[y][x] in [3, 4]:
                    for x, y in zip(range(min(start_x, end_x) + 1, max(start_x, end_x)), range(min(start_y, end_y) + 1, max(start_y, end_y))):
                        if self.game.board[y][x] == 0 and self.game.board[y+value][x+value] in [3, 4]:
                            return False
        return True
        
        
    def is_valid_move(self, start_x, start_y, end_x, end_y):
        '''
        This function verifies if the move is valid.
        
        params:
        start_x: the x-coordinate of the start , type: int
        start_y: the y-coordinate of the start , type: int
        end_x: the x-coordinate of the end , type: int
        end_y: the y-coordinate of the end , type: int
        
        return:
        True if the move is valid else False , type: bool
        '''
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
        

    def flip_pieces(self, start_x, start_y, end_x, end_y):
        '''
        This function flips the pieces when a move is valid.
        
        params:
        start_x: the x-coordinate of the start , type: int
        start_y: the y-coordinate of the start , type: int
        end_x: the x-coordinate of the end , type: int
        end_y: the y-coordinate of the end , type: int
        '''
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
        '''
        This function flips the pieces.
        
        params:
        a: the a-coordinate , type: int
        b: the b-coordinate , type: int
        '''
        if self.game.board[a][b] == 3:
            self.game.board[a][b] = 4
        elif self.game.board[a][b] == 4:
            self.game.board[a][b] = 3