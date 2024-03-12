import pygame
from pygame.locals import *
from math import*
pygame.init()

def jeu():
    largeur_ecran, hauteur_ecran = pygame.display.Info().current_w, pygame.display.Info().current_h
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
    pygame.display.set_caption("Menu")

    fond_ecran = pygame.image.load('constellation.jpeg')
    fond_ecran = pygame.transform.scale(fond_ecran, (largeur_ecran, hauteur_ecran))

    en_cours = True
    ecran.blit(fond_ecran, (0, 0))
    taille_carre = 50
    taille_cercle = 30
    while en_cours:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from menu_staryinsh import menu
                menu()
            for i in range(4):
                click_hit_box(697+(i*75), 190-(i*43), 723+(i*75), 215-(i*43), event, taille_carre, ecran)
            for i in range(7):
                click_hit_box(622+(i*75), 320-(i*43), 649+(i*75), 345-(i*43), event, taille_carre, ecran)
            for i in range(8):
                click_hit_box(622+(i*75), 405-(i*43), 649+(i*75), 435-(i*43), event, taille_carre, ecran)
            for i in range(9):
                click_hit_box(622+(i*75), 495-(i*43), 647+(i*75), 520-(i*43), event, taille_carre, ecran)      
            for i in range(10):
                click_hit_box(622+(i*75), 580-(i*43), 647+(i*75), 605-(i*43), event, taille_carre, ecran)
            for i in range(9):
                click_hit_box(697+(i*75), 625-(i*43), 723+(i*75), 650-(i*43), event, taille_carre, ecran)
            for i in range(10): 
                click_hit_box(697+(i*75), 712-(i*43), 723+(i*75), 737-(i*43), event, taille_carre, ecran)
            for i in range(9):
                click_hit_box(773+(i*75), 755-(i*43), 799+(i*75), 780-(i*43), event, taille_carre, ecran)
            for i in range(8):
                click_hit_box(848+(i*75), 800-(i*43), 873+(i*75), 825-(i*43), event, taille_carre, ecran)
            for i in range(7):
                click_hit_box(925+(i*75), 842-(i*43), 950+(i*75), 867-(i*43), event, taille_carre, ecran)
            for i in range(4):
                click_hit_box(1075+(i*75), 843-(i*43), 1100+(i*75), 867-(i*43), event, taille_carre, ecran)
            
        pygame.display.flip()
    pygame.quit()

def click_hit_box(x,y,x2,y2,event,taille_carre,ecran):
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            if x <= event.pos[0] <= x + taille_carre and y <= event.pos[1] <= y + taille_carre:
                pion_image = pygame.image.load("./pion/pion_j1.png")
                pion_image = pygame.transform.scale(pion_image, (80, 80))
                ecran.blit(pion_image, (x2-40, y2-43))
                return True
    return False


jeu()
