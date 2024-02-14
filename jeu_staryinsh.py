import pygame
from pygame.locals import *

pygame.init()

def menu():
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran), FULLSCREEN)
    pygame.display.set_caption("Menu")

    fond_ecran = pygame.image.load('fond.png')
    fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))

    ecran.blit(fond_ecran, (0, 0))
        
    pygame.display.flip()

    pygame.quit()

menu()
