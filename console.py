import pygame
from pygame.locals import *

pygame.init()

def menu():
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran), FULLSCREEN)
    pygame.display.set_caption("Menu")

    fond_ecran = pygame.image.load('fond.png')
    fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))

    bouton_demarrer_image = pygame.image.load('jouer.png')
    bouton_regle_image = pygame.image.load('regle.png')
    bouton_parametre_image = pygame.image.load('parametre.png')
    
    bouton_demarrer_image = pygame.transform.scale(bouton_demarrer_image, (800, 700))
    bouton_regle_image = pygame.transform.scale(bouton_regle_image, (600, 350))
    bouton_parametre_image = pygame.transform.scale(bouton_parametre_image, (600, 350))

    survol_demarrer = False
    survol_regle = False
    survol_parametre = False
    en_cours = True
    
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                en_cours = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 <= event.pos[0] <= 800 and 200 <= event.pos[1] <= 700:
                        print("Le jeu commence !")
                    elif 900 <= event.pos[0] <= 1100 and 300 <= event.pos[1] <= 350:
                        print("Les règles du jeu")
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                survol_demarrer = 300 <= x <= 300 + bouton_demarrer_image.get_width() and 200 <= y <= 200 + bouton_demarrer_image.get_height()
                survol_regle = 1096 <= x <= 1096 + bouton_regle_image.get_width() and 200 <= y <= 200 + bouton_regle_image.get_height()
                survol_parametre = 1096 <= x <= 1096 + bouton_parametre_image.get_width() and 549 <= y <= 549 + bouton_parametre_image.get_height()

        ecran.blit(fond_ecran, (0, 0))
        
        if survol_demarrer:
            ecran.blit(pygame.transform.scale(bouton_demarrer_image, (bouton_demarrer_image.get_width() + 10, bouton_demarrer_image.get_height() + 10)), (290, 190))
        else:
            pygame.time.wait(20)
            ecran.blit(bouton_demarrer_image, (300, 200))

        if survol_regle:
            ecran.blit(pygame.transform.scale(bouton_regle_image, (bouton_regle_image.get_width() + 10, bouton_regle_image.get_height() + 10)), (1076, 190))
        else:
            pygame.time.wait(20)
            ecran.blit(bouton_regle_image, (1096, 200))

        if survol_parametre:
            ecran.blit(pygame.transform.scale(bouton_parametre_image, (bouton_parametre_image.get_width() + 10, bouton_parametre_image.get_height() + 10)), (1076, 539))
        else:
            pygame.time.wait(20)
            ecran.blit(bouton_parametre_image, (1096, 549))
            

        pygame.display.flip()

    pygame.quit()

menu()
