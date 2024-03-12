import pygame
from pygame.locals import *
import carrouselle_img as regle
import jeu_staryinsh as jeu
import parametre_staryinsh as parametre

pygame.init()

def menu():
    #initialisation de la fenetre
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
    pygame.display.set_caption("Menu")

    #chargement de l'image de fond
    fond_ecran = pygame.image.load('fond.jpeg')
    fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))
    
    ratio_largeur = largeur_ecran / 2048
    ratio_hauteur = hauteur_ecran / 1152
    
    #charegement des images
    bouton_demarrer_image = pygame.image.load('jouer.jpg')
    bouton_regle_image = pygame.image.load('regle.jpg')
    bouton_parametre_image = pygame.image.load('parametre.jpg')
    
    #redimensionnement des images
    bouton_demarrer_image = pygame.transform.scale(bouton_demarrer_image, (800*ratio_largeur, 700*ratio_hauteur))
    bouton_regle_image = pygame.transform.scale(bouton_regle_image, (800*ratio_largeur, 350*ratio_hauteur))
    bouton_parametre_image = pygame.transform.scale(bouton_parametre_image, (800*ratio_largeur, 350*ratio_hauteur))

    #initialisation des variables
    survol_demarrer = False
    survol_regle = False
    survol_parametre = False
    en_cours = True
    
    # s'occupe des evenements
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                en_cours = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 1046*ratio_largeur <= event.pos[0] <= 1796*ratio_largeur and 200*ratio_hauteur <= event.pos[1] <= 550*ratio_hauteur:
                        regle.carrousel()
                    if 250*ratio_largeur <= event.pos[0] <= 1050*ratio_largeur and 200*ratio_hauteur <= event.pos[1] <= 900*ratio_hauteur:
                        jeu.jeu()
                    if 1046*ratio_largeur <= event.pos[0] <= 1646*ratio_largeur and 549*ratio_hauteur <= event.pos[1] <= 899*ratio_hauteur:
                        parametre.parametre()
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                survol_demarrer = 250*ratio_largeur <= x <= 250*ratio_largeur + bouton_demarrer_image.get_width() and 200*ratio_hauteur <= y <= 200*ratio_hauteur + bouton_demarrer_image.get_height()
                survol_regle = 1046*ratio_largeur <= x <= 1046*ratio_largeur + bouton_regle_image.get_width() and 200*ratio_hauteur <= y <= 200*ratio_hauteur + bouton_regle_image.get_height()
                survol_parametre = 1046*ratio_largeur <= x <= 1046*ratio_largeur + bouton_parametre_image.get_width() and 549*ratio_hauteur <= y <= 549*ratio_hauteur + bouton_parametre_image.get_height()

        ecran.blit(fond_ecran, (0, 0))
        
        
        # Affichage des boutons pour les placer au bon endroit sur l'écran
        if survol_demarrer:
            ecran.blit(pygame.transform.scale(bouton_demarrer_image, (bouton_demarrer_image.get_width() + 15, bouton_demarrer_image.get_height() + 15)), (245*ratio_largeur, 195*ratio_hauteur))
        else:
            pygame.time.wait(20)
            ecran.blit(bouton_demarrer_image, (250*ratio_largeur, 200*ratio_hauteur))

        if survol_regle:
            ecran.blit(pygame.transform.scale(bouton_regle_image, (bouton_regle_image.get_width() + 15, bouton_regle_image.get_height() + 15)), (1046*ratio_largeur, 190*ratio_hauteur))
        else:
            pygame.time.wait(20)
            ecran.blit(bouton_regle_image, (1046*ratio_largeur, 200*ratio_hauteur))

        if survol_parametre:
            ecran.blit(pygame.transform.scale(bouton_parametre_image, (bouton_parametre_image.get_width() + 15, bouton_parametre_image.get_height() + 15)), (1046*ratio_largeur, 549*ratio_hauteur))
        else:
            pygame.time.wait(20)
            ecran.blit(bouton_parametre_image, (1046*ratio_largeur, 549*ratio_hauteur))
            

        pygame.display.flip()

    pygame.quit()

menu()
