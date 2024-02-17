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
                from menu_staryinsh import menu
                menu()
            
                            
        ecran.blit(fond_ecran, (0, 0))
        pygame.display.flip()

    pygame.quit()