import pygame
import pygame_widgets
from pygame.locals import *
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()

def parametre():
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
    pygame.display.set_caption("Menu")
    fond_ecran = pygame.image.load('fond.jpeg')
    fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))
    
    slider = Slider(ecran, 1700, 200, 300, 20, min=0, max=100, step=1)
    sortie = TextBox(ecran, 1600, 185, 65, 50, fontSize=30)

    sortie.disable()
    
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                en_cours = False

        sortie.setText(str(slider.getValue()))

        pygame_widgets.update(event)
        pygame.display.update()
        
        ecran.blit(fond_ecran, (0, 0))
        pygame.display.flip()


