import pygame
from pygame.locals import *
import os

def charger_images(largeur_ecran, hauteur_ecran):
    dossier_images = 'images'
    fichiers_images = os.listdir(dossier_images)
    images = [pygame.image.load(os.path.join(dossier_images, img)) for img in fichiers_images]
    images = [pygame.transform.scale(img, (largeur_ecran, hauteur_ecran)) for img in images]
    return images

def carrousel():
    pygame.init()
    
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

    pygame.display.set_caption("Carrousel d'images")
    
    regle_image = pygame.image.load('images/regle1.jpg')
    regle_image = pygame.transform.scale(regle_image, (largeur_ecran, hauteur_ecran))
    ecran.blit(regle_image, (0, 0))
    pygame.display.flip()

    images = charger_images(largeur_ecran, hauteur_ecran)

    position_carrousel_x = 0
    indice_image_actuelle = 0

    marge_gauche_bouton = 0.655
    marge_droite_bouton = 0.48
    marge_basse_bouton = 0.2

    largeur_bouton = int(largeur_ecran * 0.15)
    hauteur_bouton = int(hauteur_ecran * 0.1)

    bouton_suivant = pygame.transform.scale(pygame.image.load('suivant_button.png'), (largeur_bouton, hauteur_bouton))
    bouton_precedent = pygame.transform.scale(pygame.image.load('precedent_button.png'), (largeur_bouton, hauteur_bouton))

    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from menu_staryinsh import menu
                menu()
                return
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                survol_bouton_precedent = largeur_ecran - largeur_ecran * marge_gauche_bouton <= x <= largeur_ecran - largeur_ecran * marge_gauche_bouton + largeur_bouton and hauteur_ecran - hauteur_ecran * marge_basse_bouton <= y <= hauteur_ecran - hauteur_ecran * marge_basse_bouton + hauteur_bouton
                survol_bouton_suivant = largeur_ecran - largeur_ecran * marge_droite_bouton <= x <= largeur_ecran - largeur_ecran * marge_droite_bouton + largeur_bouton and hauteur_ecran - hauteur_ecran * marge_basse_bouton <= y <= hauteur_ecran - hauteur_ecran * marge_basse_bouton + hauteur_bouton

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if survol_bouton_suivant:
                        indice_image_actuelle = (indice_image_actuelle + 1) % len(images)
                        position_carrousel_x = -indice_image_actuelle * largeur_ecran
                    elif survol_bouton_precedent:
                        indice_image_actuelle = (indice_image_actuelle - 1) % len(images)
                        position_carrousel_x = -indice_image_actuelle * largeur_ecran

        for i, image in enumerate(images):
            position_image_x = i * largeur_ecran + position_carrousel_x
            transition_x = max(0, min(largeur_ecran, position_image_x))
            ecran.blit(image, (transition_x, 0))

        if survol_bouton_suivant:
            ecran.blit(pygame.transform.scale(bouton_suivant, (bouton_suivant.get_width() + 15, bouton_suivant.get_height() + 15)), (largeur_ecran - largeur_ecran * marge_droite_bouton - 7, hauteur_ecran - hauteur_ecran * marge_basse_bouton - 7))
        else:
            ecran.blit(bouton_suivant, (largeur_ecran - largeur_ecran * marge_droite_bouton, hauteur_ecran - hauteur_ecran * marge_basse_bouton))

        if survol_bouton_precedent:
            ecran.blit(pygame.transform.scale(bouton_precedent, (bouton_precedent.get_width() + 15, bouton_precedent.get_height() + 15)), (largeur_ecran - largeur_ecran * marge_gauche_bouton - 7, hauteur_ecran - hauteur_ecran * marge_basse_bouton - 7))
        else:
            ecran.blit(bouton_precedent, (largeur_ecran - largeur_ecran * marge_gauche_bouton, hauteur_ecran - hauteur_ecran * marge_basse_bouton))

        pygame.display.flip()

    pygame.quit()

