import pygame
from pygame.locals import *
from math import*

class Game:
    def __init__(self):
        self.board = [[0 for i in range(10)] for j in range(10)]
        self.player = 1
        self.nb_pions_places = 0
        self.pion_image = pygame.image.load("./pion/pion_j1.png")
        self.pion_image = pygame.transform.scale(self.pion_image, (80, 80))

    
    
    
    def click_hit_box(self, x, y, x2, y2, event, taille_carre, ecran, i, j):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if x <= event.pos[0] <= x + taille_carre and y <= event.pos[1] <= y + taille_carre:
                    if self.board[j][i] != 0:
                        return False
                    self.nb_pions_places += 1
                    ecran.blit(self.pion_image, (x2-40, y2-43))
                    self.board[j][i] = 1
                    return True
        return False

    
    def afficher_board(self):
        for row in self.board:
            print(row)
            
    def jeu(self):
        pygame.init()
        largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
        ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
        pygame.display.set_caption("Menu")

        fond_ecran = pygame.image.load('constellation.jpeg')
        fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))

        en_cours = True
        ecran.blit(fond_ecran, (0, 0))
        taille_carre = 50
        while en_cours:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    from menu_staryinsh import menu
                    menu()
                for i in range(4):
                    j=0
                    self.click_hit_box(697+(i*75), 190-(i*43), 723+(i*75), 215-(i*43), event, taille_carre, ecran,i,j)
                for i in range(7):
                    j=1
                    self.click_hit_box(622+(i*75), 320-(i*43), 649+(i*75), 345-(i*43), event, taille_carre, ecran,i,j)
                for i in range(8):
                    j=2
                    self.click_hit_box(622+(i*75), 405-(i*43), 649+(i*75), 435-(i*43), event, taille_carre, ecran,i,j)
                for i in range(9):
                    j=3
                    self.click_hit_box(622+(i*75), 495-(i*43), 647+(i*75), 520-(i*43), event, taille_carre, ecran,i,j)      
                for i in range(10):
                    j=4
                    self.click_hit_box(622+(i*75), 580-(i*43), 647+(i*75), 605-(i*43), event, taille_carre, ecran,i,j)
                for i in range(9):
                    j=5
                    self.click_hit_box(697+(i*75), 625-(i*43), 723+(i*75), 650-(i*43), event, taille_carre, ecran,i,j)
                for i in range(10): 
                    j=6
                    self.click_hit_box(697+(i*75), 712-(i*43), 723+(i*75), 737-(i*43), event, taille_carre, ecran,i,j)
                for i in range(9):
                    j=7
                    self.click_hit_box(773+(i*75), 755-(i*43), 799+(i*75), 780-(i*43), event, taille_carre, ecran,i,j)
                for i in range(8):
                    j=8
                    self.click_hit_box(848+(i*75), 800-(i*43), 873+(i*75), 825-(i*43), event, taille_carre, ecran,i,j)
                for i in range(7):
                    j=9
                    self.click_hit_box(925+(i*75), 842-(i*43), 950+(i*75), 867-(i*43), event, taille_carre, ecran,i,j)
                for i in range(4):
                    j=10
                    self.click_hit_box(1075+(i*75), 843-(i*43), 1100+(i*75), 867-(i*43), event, taille_carre, ecran,i,j)
                    
                pygame.display.flip()
                
                if self.nb_pions_places==10:  # À définir selon vos besoins
                    self.afficher_board()
                    en_cours = False
        pygame.quit()



def launch_game():
    game = Game()
    game.jeu()


launch_game()