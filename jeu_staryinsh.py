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
    while en_cours:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                from menu_staryinsh import menu
                menu()
            for i in range(4):
                Hexagon(723+(i*75), 220-(i*43), 30).draw(ecran)
            for i in range(7):
                Hexagon(647+(i*75), 345-(i*43), 30).draw(ecran)
            for i in range(8):
                Hexagon(647+(i*75), 435-(i*43), 30).draw(ecran)
            for i in range(9):
                Hexagon(647+(i*75), 520-(i*43), 30).draw(ecran)                  
            for i in range(10):
                Hexagon(647+(i*75), 605-(i*43), 30).draw(ecran) 
            for i in range(9):
                Hexagon(723+(i*75), 650-(i*43), 30).draw(ecran) 
            for i in range(10):
                Hexagon(723+(i*75), 737-(i*43), 30).draw(ecran) 
            for i in range(9):
                Hexagon(797+(i*75), 780-(i*43), 30).draw(ecran) 
            for i in range(8):
                Hexagon(873+(i*75), 825-(i*43), 30).draw(ecran) 
            for i in range(7):
                Hexagon(950+(i*75), 867-(i*43), 30).draw(ecran) 
            for i in range(4):
                Hexagon(1100+(i*75), 867-(i*43), 30).draw(ecran)
                    
        pygame.display.flip()
    pygame.quit()

class Hexagon:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.points = self.calculate_points()

    def calculate_points(self):
        points = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = pi / 180 * angle_deg
            points.append((self.x + self.size * cos(angle_rad),self.y + self.size * sin(angle_rad)))
        return points

    def draw(self, surface, color=(255, 255, 255)):
        pygame.draw.polygon(surface, color, self.points)

    def is_point_inside(self, point):
        x, y = point
        return pygame.Rect(self.x - self.size, self.y - self.size, 2*self.size, 2*self.size).collidepoint(x, y)
     
    
jeu()