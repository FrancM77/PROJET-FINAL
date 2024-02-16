import pygame
from pygame.locals import *

pygame.init()

def jeu():
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
    pygame.display.set_caption("Menu")

    fond_ecran = pygame.image.load('constellation.jpeg')
    fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))

    en_cours = True
    
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                en_cours = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 <= event.pos[0] <= 1100 and 200 <= event.pos[1] <= 900:
                        if 300 <= event.pos[0] <= 1100 and 200 <= event.pos[1] <= 900:
                            print("Le jeu commence !")
                        elif 1096 <= event.pos[0] <= 1696 and 200 <= event.pos[1] <= 550:
                            print("Les règles du jeu")
                        elif 1096 <= event.pos[0] <= 1696 and 549 <= event.pos[1] <= 899:
                            print("Les paramètres")    
                            
        ecran.blit(fond_ecran, (0, 0))
        pygame.display.flip()

    pygame.quit()