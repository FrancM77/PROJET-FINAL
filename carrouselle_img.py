import pygame
from pygame.locals import *
import os

pygame.init()

largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

dossier_images = 'images'
fichiers_images = os.listdir(dossier_images)
images = [pygame.image.load(os.path.join(dossier_images, img)) for img in fichiers_images]
images = [pygame.transform.scale(img, (largeur_ecran, hauteur_ecran)) for img in images]

pygame.display.set_caption("Carrousel d'images")

position_carrousel_x = 0
indice_image_actuelle = 0

image_bouton_suivant = pygame.image.load('suivant_button.png')
bouton = pygame.transform.scale(image_bouton_suivant, (250, 110))

en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
                en_cours = False
        elif event.type == MOUSEMOTION:
            souris_x, souris_y = event.pos
            bouton_suivant = image_bouton_suivant.get_rect()
            bouton_suivant.x = largeur_ecran - 1150
            bouton_suivant.y = hauteur_ecran - 235
            survol_bouton = bouton_suivant.collidepoint(souris_x, souris_y)
            
        elif event.type == MOUSEBUTTONDOWN:
            souris_x, souris_y = event.pos
            bouton_suivant = image_bouton_suivant.get_rect()
            bouton_suivant.x = largeur_ecran - 1150
            bouton_suivant.y = hauteur_ecran - 235
            if bouton_suivant.collidepoint(souris_x, souris_y):
                indice_image_actuelle = (indice_image_actuelle + 1) % len(images)
                position_carrousel_x = -indice_image_actuelle * largeur_ecran
    for i, image in enumerate(images):
        position_image_x = i * largeur_ecran + position_carrousel_x
        transition_x = max(0, min(largeur_ecran, position_image_x))
        ecran.blit(image, (transition_x, 0))
    
    if survol_bouton:
        ecran.blit(pygame.transform.scale(bouton, (bouton.get_width() + 15, bouton.get_height() + 15)), (largeur_ecran - 1150 - 7  , hauteur_ecran - 235 - 7))
    else:
        ecran.blit(bouton, (largeur_ecran - 1150, hauteur_ecran - 235))
   
    pygame.display.flip()

pygame.quit()
