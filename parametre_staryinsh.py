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
    
    image_bouton_suivant = pygame.image.load('suivant_button.png')
    bouton_suiv = pygame.transform.scale(image_bouton_suivant, (250, 110))

    image_bouton_precedent = pygame.image.load('precedent_button.png')
    bouton_prec = pygame.transform.scale(image_bouton_precedent, (300, 110))
    
    slider = Slider(ecran, 1700, 200, 300, 20, min=0, max=100, step=1)
    sortie = TextBox(ecran, 1600, 185, 65, 50, fontSize=30)

    sortie.disable()
    
    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                en_cours = False
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                survol_bouton_precedent = largeur_ecran - 1335 <= x <= largeur_ecran - 1335 + bouton_prec.get_width() and hauteur_ecran - 230 <= y <= hauteur_ecran - 230 + bouton_prec.get_height()
                survol_bouton_suivant = largeur_ecran - 950 <= x <= largeur_ecran - 950 + bouton_suiv.get_width() and hauteur_ecran - 230 <= y <= hauteur_ecran - 230 + bouton_suiv.get_height()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if survol_bouton_suivant:
                        largeur_ecran = 1920
                        hauteur_ecran = 1080
                        ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
                    elif survol_bouton_precedent:
                        largeur_ecran = 2560
                        hauteur_ecran = 1440
                        ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

        sortie.setText(str(slider.getValue()))

        pygame_widgets.update(event)
        pygame.display.update()
        
        ecran.blit(fond_ecran, (0, 0))
        ecran.blit(bouton_suiv, (largeur_ecran - 950, hauteur_ecran - 230))
        ecran.blit(bouton_prec, (largeur_ecran - 1335, hauteur_ecran - 230))
        pygame.display.flip()


