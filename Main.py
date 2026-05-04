import pygame
import random
pygame.init() #initialiserar pygame

screen=pygame.display.set_mode((800,600)) #Skapar ett fönster med storleken 500x500
pygame.display.set_caption("Snake") #Sätter en titel på fönstret

running=True
while running:#Skapar en loop som gör att programmet inte stängs ned direkt
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #Gör att programmet kan stängas ned genom att klicka på krysset
            running=False

    screen.fill((255,255,255))#Fyller i fönstret med vald RGB färg
    pygame.display.flip()#updatear hela skärmen istället för bara en del av den

pygame.quit()


class GameObject():#Skapar en klass som heter GameObject
    def __init__(self,x,y,bredd,höjd):#initialiserar klassen med valda variabler
        self.rect=pygame.rect(x,y,bredd,höjd)#Definerar variablerna




class Snake(GameObject): #skapar en subklass för ormen som ärver av GameObject
    def __init__(self,x,y):
        super.__init__(self,x,y,50,50)#Gör så att du ärver värdena från Parentclassen
        self.color=pygame.Color(0,255,12)#Ritar en rectangel på skärmen som är Grön med en tint av blå
        self.direction=(0,0)#Bestämmer start variablerna för ormens riktning
        self.expansion=[[x,y]]#Skapar variabler för att växa ormen genom en lista
        self.grew=False #Skapar en Bool som kommer användas för att se till att ormen inte växer om inte kriterierna är uppnådda
    
    def move(self): #metod som definierar rörelse för ormen
        dx,dy=self.direction # förändring i x och y led 
        headX,headY=self.expansion[0] # huvudet har index 0 (längst fram)
        NewHead=[dx+headX,dy+headY] # "nya" huvudet är förändringen i x och y led + huvudet
        self.expansion.insert(0,NewHead) # sätter in "nya" huvudet i kroppen 

        if self.grew==False:
            self.expansion.pop()#Tar bort bloket bakom sig om den inte växt
        else:
            self.grew==False


    
    
    def grow(self):
        self.grew==True
    
    
class Game:
  def key_input(self):#Skapar en funktion med en dictionary av key inputs
     keys={
        pygame.K_UP:(0,-1),
        pygame.K_DOWN:(0,1),
        pygame.K_LEFT:(-1,0),
        pygame.K_RIGHT:(1,0),
        pygame.K_w:(0,-1),
        pygame.K_s:(0,1),
        pygame.K_a:(-1,0),
        pygame.K_d:(1,0)
            }
        
for event in pygame.get():
    if event.type == pygame.KEYDOWN and event.key in keys:
        self.snake(keys[event.key])