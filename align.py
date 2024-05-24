from display import Display

class Align:
    def __init__(self,game,width_ratio,height_ratio,piece_image):
        self.game = game
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.piece_image = piece_image
        self.display = Display(game,self.width_ratio,self.height_ratio,self.piece_image)
        

    #function to check if there is an alignment
    def align_check(self,start_x, start_y, x, y):
        for j in range(5):
            if self.game.board[start_y + j * y][start_x + j * x] != self.game.board[start_y][start_x]:
                return False
        return True
    
    def align_condition(self, screen):
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
    #end of function to check if there is an alignment
    
    #function to remove alignment
    def alignment_choice(self,i,j,x,y,event,square_size,screen):
        if x <= event.pos[0] <= x + square_size and y <= event.pos[1] <= y + square_size:
            i += self.game.recover_offset(j)
            for alignment in self.game.alignments:
                if (j,i) in alignment:
                    self.remove_alignment(screen, alignment)
                    self.game.multialign = False
                    break
        return False

    def remove_alignment(self, screen, alignment):
        for (j, i) in alignment:
            self.game.board[j][i] = 0
        self.display.display_piece(screen)
        self.game.remove_mode = True
        self.game.play_sound_once("alignement")
    #end of function to remove alignment
