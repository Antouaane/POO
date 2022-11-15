import pygame, sys
from pygame.locals import *
import random
from random import randint
import time
from bouton import *

pygame.init()


fenetre = pygame.display.set_mode((1000, 900))
route = pygame.image.load("road.png").convert_alpha()
bg = pygame.image.load("bg_ground.jpg").convert_alpha()

voiture = pygame.image.load("voiture.png").convert_alpha()
position_voiture = voiture.get_rect()
position_voiture.topleft = ( 500,800)






def crash():
    police = pygame.font.SysFont('John Hubbard',100)
    image_texte = police.render("game over", 1, (255,0,0))
    fenetre.blit(image_texte,(360,300))
    pygame.display.flip()
      
def pose():
    menu = pygame.image.load("pause.png").convert_alpha()
    fenetre.blit(menu,(-50,0))
    pygame.display.flip()
    
lst = ["jaune.png", "noir.png", "chevrolet.png", "enemy_car_1.png", "enemy_car_2.png"]   

class Obstacle():
    def __init__(self):
        self.x = randint(180,850)
        self.y = 0
        self.image = random.choice(lst)
        self.obstacle = pygame.image.load(self.image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = randint(15,30)
        self.score = 0
      
    
        
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)
        
    def bouge(self):
        self.y += self.speed
        if self.y >900:
            self.speed = randint(25,40)
            back = randint(1200,2200)
            self.y -= back
            self.x = randint(180,850)
            
        
            
            
    def collision(self):
        x_voiture = position_voiture[0]
        y_voiture = position_voiture[1]

        if (self.x-30) <= x_voiture <= (self.x+30)  and (self.y-30)<= y_voiture <=(self.y+30):
            crash()
            time.sleep(3)
        menu()
            
            
            
            
            
            
            
            
class Piece():
    def __init__(self,image):
        self.x = randint(180,850)
        self.y = 0
        self.obstacle = pygame.image.load(image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = randint(15,20)
        self.score = 0
    
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)  
        
    def bouge(self):
        self.y += self.speed
        if self.y >900:
            self.speed = randint(15,25)
            back = randint(1200,2200)
            self.y -= back
            self.x = randint(180,850)
    
    
    def collision(self):
        x_voiture = position_voiture[0]
        y_voiture = position_voiture[1]

        if (self.x-20) <= x_voiture <= (self.x+20)  and (self.y-20)<= y_voiture <=(self.y+20):
            self.score += 1
            
    def highscore(self,x,y):
        font = pygame.font.SysFont("arial", 55)
        text = font.render("Score: " + str(self.score), True, "white")
        fenetre.blit(text, (x, y))
            
            
            



piece = Piece("piece.png")


lst_voiture = [Obstacle() for _ in range(2)]
pas_deplacement = 20



def jeu():
    y_bg = 0
    while True:
        global position_voiture
        
        x = position_voiture[0]
        y = position_voiture[1]      
        
        y_bg +=18
        
        if y_bg < 900:
            fenetre.blit(route, (0,y_bg))
            fenetre.blit(route, (0,y_bg-900))
        else:
            y_bg = 0
            fenetre.blit(route, (0,y_bg))
            
            
            
        if  x <= 130:
            position_voiture = position_voiture.move(pas_deplacement,0)
            
            
        if x >= 810 :
            position_voiture = position_voiture.move(-pas_deplacement,0)   
            

        fenetre.blit(voiture, position_voiture)
        piece.affichage()
        piece.bouge()
        piece.collision()
        piece.highscore(770,0)
      


        for obs in lst_voiture:
               obs.affichage()
               obs.bouge()
               obs.collision()
               
               
        for event in pygame.event.get() :
            if event.type == KEYDOWN:

                if event.key == K_RIGHT : 
                    position_voiture = position_voiture.move(pas_deplacement,0)

                if event.key == K_LEFT : 
                    position_voiture = position_voiture.move(-pas_deplacement,0)
                    
                if event.key == K_UP:
                    pause = True
                    while pause:
                        pose()
                        for event in pygame.event.get():
                            if event.type==KEYDOWN and event.key ==  K_SPACE:
                                pause = False
                                break

                    

            
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        

        
        clock.tick(30)
        pygame.display.flip()
def get_police(size): 
    return pygame.font.Font("font.ttf", size)

def option():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        fenetre.fill("black")

        OPTIONS_TEXT = get_police(15).render("Règles : Déplace ta voiture pour récupérer les pieces ! Mais attention aux autres voitures !", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 50))
        fenetre.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        OPTIONS_TEXT_1 = get_police(15).render("Option: Press Fleche from the top to pause the game", True, "white")
        OPTIONS_RECT_1 = OPTIONS_TEXT_1.get_rect(center=(500, 200))
        fenetre.blit(OPTIONS_TEXT_1, OPTIONS_RECT_1)

        OPTIONS_BACK = Bouton(None, (500, 460), "RETOUR", get_police(75), "white")
        OPTIONS_BACK.update(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                     menu()

        pygame.display.flip()
        
def menu():
    while True:
        fenetre.blit(bg, (-100,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        MENU_TEXT = get_police(100).render("MENU", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center = (550, 80))
        
        start_bouton = Bouton(pygame.image.load("Play Rect.png"), (530, 250), "PLAY", get_police(75), "#000000")
        option_bouton = Bouton(pygame.image.load("Options Rect.png"), (530, 400), "OPTIONS", get_police(75), "#000000")
        leave_bouton = Bouton(pygame.image.load("Quit Rect.png"), (530, 550),"QUIT", get_police(75), "#000000")
        
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if start_bouton.checkForInput(MENU_MOUSE_POS):
                    jeu()
                    
                if option_bouton.checkForInput(MENU_MOUSE_POS):
                    option()
                    
                if leave_bouton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        
        
        
        for button in [start_bouton, option_bouton, leave_bouton]:
            button.update(fenetre)
        
        
        fenetre.blit(MENU_TEXT, MENU_RECT)
        pygame.display.flip()
    
        
menu()
