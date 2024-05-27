from display import Display

class Align:
    '''
    This class is used to check if there is an alignment and remove it.
    '''
    def __init__(self,game,width_ratio,height_ratio,piece_image):
        '''
        This function initializes the align object.
        
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
        

    def align_check(self,start_x, start_y, x, y):
        '''
        This function checks if there is an alignment.
        
        params:
        start_x: the x-coordinate of the starting point , type: int
        start_y: the y-coordinate of the starting point , type: int
        x: the x-coordinate of the direction , type: int
        y: the y-coordinate of the direction , type: int
        
        return:
        True if there is an alignment, False otherwise , type: bool
        '''
        for j in range(5):
            if self.game.board[start_y + j * y][start_x + j * x] != self.game.board[start_y][start_x]:
                return False
        return True
    
    def align_condition(self, screen):
        '''
        This function checks if there is an alignment and removes it.
        
        params:
        screen: the screen to display the pieces on , type: pygame.Surface
        
        return:
        True if there is an alignment, False otherwise , type: bool
        '''
        self.game.alignments = []
        for j in range(11):
            for i in range(11):
                if self.game.board[j][i] in [3, 4]:  
                    player_owner = 2 if self.game.board[j][i] == 4 else 1
                    # line (-)
                    if i <= 6 and self.align_check(i, j, 1, 0):
                        if player_owner == self.game.player:
                            alignment = [(j, i + k) for k in range(5)]
                            self.game.alignments.append(alignment)
                    
                    # column (|)
                    if j <= 6 and self.align_check(i, j, 0, 1):
                        if player_owner == self.game.player:
                            alignment = [(j + k, i) for k in range(5)]
                            self.game.alignments.append(alignment)
                    
                    # Diagonal (\)
                    if j <= 6 and i <= 6 and self.align_check(i, j, 1, 1):
                        if player_owner == self.game.player:
                            alignment = [(j + k, i + k) for k in range(5)]
                            self.game.alignments.append(alignment)
        if len(self.game.alignments) == 1:
            self.remove_alignment(screen, self.game.alignments[0])
            return True
        elif len(self.game.alignments) > 1:
            self.game.multialign = True
            return True
        return False
    
    
    def alignment_choice(self,i,j,x,y,event,square_size,screen):
        '''
        This function choose an alignment to remove if there is multialignment from the board.
        
        params:
        i: the i-coordinate of the piece on the board , type: int
        j: the j-coordinate of the piece on the board , type: int
        x: the x-coordinate of the piece , type: int
        y: the y-coordinate of the piece , type: int
        event: the event to handle , type: pygame.event
        square_size: the size of the square , type: int
        screen: the screen to display the piece on , type: pygame.Surface
        
        return:
        True if the AI player has removed an alignment else False , type: bool
        '''
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.game.recover_offset(j)
            for alignment in self.game.alignments:
                if (j,i) in alignment:
                    self.remove_alignment(screen, alignment)
                    self.game.multialign = False
                    return True
        return False

    def remove_alignment(self, screen, alignment):
        '''
        This function removes an alignment from the board.
        
        params:
        screen: the screen to display the piece on , type: pygame.Surface
        alignment: the alignment to remove , type: list of tuples
        '''
        for (j, i) in alignment:
            self.game.board[j][i] = 0
        self.display.display_piece(screen)
        self.game.remove_mode = True
        self.game.play_sound_once("alignement")