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

    image_bouton_suivant = pygame.image.load('suivant_button.png')
    bouton_suiv = pygame.transform.scale(image_bouton_suivant, (250, 110))

    image_bouton_precedent = pygame.image.load('precedent_button.png')
    bouton_prec = pygame.transform.scale(image_bouton_precedent, (300, 110))


    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from menu_staryinsh import menu
                menu()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                survol_bouton_precedent = largeur_ecran - 1335 <= x <= largeur_ecran - 1335 + bouton_prec.get_width() and hauteur_ecran - 230 <= y <= hauteur_ecran - 230 + bouton_prec.get_height()
                survol_bouton_suivant = largeur_ecran - 950 <= x <= largeur_ecran - 950 + bouton_suiv.get_width() and hauteur_ecran - 230 <= y <= hauteur_ecran - 230 + bouton_suiv.get_height()

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
            ecran.blit(pygame.transform.scale(bouton_suiv, (bouton_suiv.get_width() + 15, bouton_suiv.get_height() + 15)), (largeur_ecran - 950 - 7, hauteur_ecran - 230 - 7))
        else:
            ecran.blit(bouton_suiv, (largeur_ecran - 950, hauteur_ecran - 230))

        if survol_bouton_precedent:
            ecran.blit(pygame.transform.scale(bouton_prec, (bouton_prec.get_width() + 15, bouton_prec.get_height() + 15)), (largeur_ecran - 1335 - 7, hauteur_ecran - 230 - 7))
        else:
            ecran.blit(bouton_prec, (largeur_ecran - 1335, hauteur_ecran - 230))

        pygame.display.flip()

    pygame.quit()

