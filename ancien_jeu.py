import pygame, sys
from pygame.locals import *
from random import randint
import time 

pygame.init()
pygame.key.set_repeat(50)

HAUTEUR = 1050
LARGEUR = 1680

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR)) # c'est mieux de mettre de varible

route = pygame.image.load("route5.png").convert_alpha()
voiture = pygame.image.load("voiture.png").convert_alpha()
position_voiture = voiture.get_rect()
position_voiture.topleft = (5*(LARGEUR//10), 2*(HAUTEUR//3))


def crash():
    police = pygame.font.SysFont('monospace', 100)
    image_texte = police.render("game over", 1, (255, 0, 0))
    fenetre.blit(image_texte, (500, 300))
    pygame.display.flip()

    
def start(): # positionnement des affichages en fonction des variables H/L
    police = pygame.font.SysFont('monospace', 100)
    image_texte = police.render("3", 1, (255, 0, 0))
    fenetre.blit(image_texte,(3*(LARGEUR//10), HAUTEUR//3))
    pygame.display.flip()
    time.sleep(1)
    police = pygame.font.SysFont('monospace', 100)
    image_texte = police.render("2", 1, (255, 79, 0))
    fenetre.blit(image_texte,(5*(LARGEUR//10), HAUTEUR//3))
    pygame.display.flip()
    time.sleep(1)
    police = pygame.font.SysFont('monospace', 100)
    image_texte = police.render("1", 1, (0, 255, 0))
    fenetre.blit(image_texte,(7*(LARGEUR//10), HAUTEUR//3))
    pygame.display.flip()
    time.sleep(1)
    police = pygame.font.SysFont('monospace', 100)
    image_texte = police.render("GO !!!", 1, (0, 255, 0))
    fenetre.blit(image_texte,(4*(LARGEUR//10), 2*(HAUTEUR//3)))
    pygame.display.flip()
    time.sleep(1)


class Obstacle():
    def __init__(self, image):
        self.x = randint(LARGEUR//5, 4*(LARGEUR//5) - 100) # -100 pour pas que le rondin dépasse la pygame.line
        self.y = -100
        self.obstacle = pygame.image.load(image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = 5
    
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)

    def mouvement(self):
        self.y += self.speed
        if self.y >= LARGEUR:
            self.y = 0
            self.x = randint(LARGEUR//5, 4*(LARGEUR//5) - 100)

    def collision(self):
        x = position_voiture[0]
        y = position_voiture[1]
    
        if (voiture_obstacle.x - 30)  <= police.x <= (voiture_obstacle.x + 30):
            police.x += 30
            
        if (self.x - 30) <= x <= (self.x + 30)  and (self.y - 30) <= y <= (self.y + 30):
            crash()
            time.sleep(2)
            pygame.display.quit()
            sys.exit()
            
            
police = Obstacle("chevrolet.png")
lst_police = [police for k in range(3)]
voiture_obstacle = Obstacle("car.png")
lst_voiture_obstacle = [voiture_obstacle for k in range(3)]

pas_deplacement = 22
y_bg = 0
     

start()


while True:
    y_bg += 5
    fenetre.fill([10,186,181])
     
    if y_bg < HAUTEUR:
        fenetre.blit(route, (0, y_bg))
        fenetre.blit(route, (0, y_bg - HAUTEUR))
    else:
        y_bg = 0
        fenetre.blit(route, (0, y_bg))  
    fenetre.blit(voiture, position_voiture)
    
    for obs in lst_police:
        obs.affichage()
        obs.mouvement()
        obs.collision()
    
    for obs in lst_voiture_obstacle:
        obs.affichage()
        obs.mouvement()
        obs.collision()
              
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT: 
                position_voiture = position_voiture.move(pas_deplacement, 0)

            if event.key == K_LEFT: 
                position_voiture = position_voiture.move(-pas_deplacement, 0)  
        
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    
    pygame.draw.line(fenetre,(0, 0, 0), [LARGEUR//5, 0], [LARGEUR//5, HAUTEUR], 10)
    pygame.draw.line(fenetre,(0, 0, 0), [4*(LARGEUR//5), 0], [4*(LARGEUR//5), HAUTEUR], 10)
    pygame.draw.line(fenetre,(0, 0, 0), [LARGEUR//5, 120], [0, 120], 10) # je rajoute une barre sous le "Niveau 1" (c'est purement estétique)
    test1 = pygame.font.SysFont('monospace', 50)
    image_texte = test1.render("Niveau 1", 5, (0, 0, 0))
    fenetre.blit(image_texte, (30, 30))
    fenetre.blit(voiture, position_voiture)
    
    pygame.display.flip()
