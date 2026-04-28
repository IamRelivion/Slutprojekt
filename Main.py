import pygame
pygame.init() #initialiserar pygame

screen=pygame.display.set_mode((500,500)) #Skapar ett fönster med storleken 500x500
pygame.display.set_caption("Snake") #Sätter en titel på fönstret

running=True
while running:#Skapar en loop som gör att programmet inte stängs ned direkt
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #Gör att programmet kan stängas ned genom att klicka på krysset
            running=False

    screen.fill((255,255,255))#Fyller i fönstret med vald RGB färg
    snake=pygame.draw.rect(screen,(0,255,120),pygame.Rect(230,225,25,25))#Ritar en rectangel på skärmen som är Grön
    pygame.display.flip()#updatear hela skärmen istället för bara en del av den

pygame.quit()


class GameObject():#Skapar en klass som heter GameObject
    def __init__(self,x,y,bredd,höjd):#initialiserar klassen med valda variabler
        self.rect=pygame.rect(x,y,bredd,höjd)#Definerar variablerna


class Snake(GameObject): #skapar en subklass för ormen som ärver av GameObject
    def __init__(self,x,y):
        super.__init__(self,x,y,50,50)#Gör så att du ärver värdena från Parentclassen
        self.color="Green"

    def move(self,dx,dy): # metod som definierar rörelse för ormen
        self.rect.x+=dx
        self.rect.y+=dy
    
    def draw(self,)
        
        
