import pygame
import random
import unittest
class Gameobject:# Parentclass för alla spelobjekt där alla objekt är rektanglar
    def __init__(self,x,y,width,height):
        self.Rect=pygame.Rect(x,y,width,height)

class Snake(Gameobject): #Childclass för ormen
    def __init__(self,x,y):
        super().__init__(x,y,50,50)
        self.color=pygame.Color(0,255,12) #Grön med en liten del blå i sig
        self.direction=(0,0) # bestämmer riktningen som ormen börjar
        self.body=[[x,y]] # För att lätt kunna öka ormen i storlek och få rörelsen att se bra ut representeras kroppen av en lista
        self.grew=False

    def move(self)->None:
        dx,dy=self.direction # förändringar i x och y led
        head_x,head_y=self.body[0] # huvudet har index 0 (längst fram på ormen)
        new_head=[head_x+dx,head_y+dy] # I takt med att ormen rör sig ersätter ett "nytt" huvud den sträckan som den rör sig
        self.body.insert(0,new_head) # för visa förändringen ovan sätts det "nya" huvudet in i listan med index 0

        if self.grew==False:
            self.body.pop() # Om ormen inte har växt tar den bort det sista elementet i listan vilket simulerar att ormen rör sig
        else:
            self.grew=False

    def grow(self)->None:
        self.grew=True

    def change_direction(self,new_direction):
        opposite=(-new_direction[0],-new_direction[1]) #motsatt riktningnen definieras som en tuple av de negativa nya riktningarna
        if opposite!=self.direction: #Kollar ifall den nya riktningen inte är densamma som den motsatta
            self.direction=new_direction
    def head(self): #definierar huvudet som index noll av kroppen
        return self.body[0]

    def check_colision(self): #kollision är detsamma som att huvudet befinner sig i kroppen(att den överlappar med något index efter noll
        return self.head() in self.body[1:]

    def draw(self,screen)->None: #
        for segment in self.body:
            x,y=segment
            pygame.draw.rect(screen,self.color,pygame.Rect(x,y,100,50))

class Apple(Gameobject):
    def __init__(self,grid_w,grid_h):
        self.grid_w=grid_w
        self.grid_h=grid_h
        self.position=self.randompos()

    def randompos(self):# ger äpplena random koordinater utifrån ett rutnät
        x=random.randint(0,self.grid_w-1)
        y=random.randint(0,self.grid_h-1)
        return [x,y]
    def respawn(self,avoid_pos)->None: # definierar respawn för äpplena
        pos=self.randompos() #
        while pos in avoid_pos:
            pos=self.randompos()
        self.position=pos

class Game: # egen game class för att alla inputs och animation ska funka
    cell=24 #pixelstorlek per cell
    grid_w=32 #antal celler horisiontellt
    grid_h=24 #antal celler veritkalt
    fps=10 #spelhastigheten
    """
    Lade till en score counter som automatiskt updaterar 
    """
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((800,600))
        self.clock=pygame.time.Clock()
        self.snake=Snake(self.grid_w//2,self.grid_h//2)
        self.apple=Apple(self.grid_w,self.grid_h)
        self.score=0
        self.font=pygame.font.SysFont("Arial",20)
        self.running=True

    def key_inputs(self)->None:
        dirs={
            pygame.K_UP:(0,-1),
            pygame.K_DOWN:(0,1),
            pygame.K_LEFT:(-1,0),
            pygame.K_RIGHT:(1,0),
            pygame.K_w:(0,-1),
            pygame.K_s:(0,1),
            pygame.K_a:(-1,0),
            pygame.K_d:(1,0)
        } # Key inputs sparas som en dictionary
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# Kollar ifall användaren trycker på krysset och stänger ner spelet därefter
                self.running=False

            if event.type == pygame.KEYDOWN and event.key in dirs: # kollar ifall någon av tangenterna ovan trycks ned
                self.snake.change_direction(dirs[event.key]) #utför rörelsen enligt den tangent som trycks ner

    def update(self)->None:
        self.snake.move()
        if self.snake.head()==self.apple.position: # kolla ifall huvudet och äpplet har samma koordinater
            self.snake.grow() # ormen växer
            self.apple.respawn(self.snake.body) # äpplet respawnar på en random koordinat
            self.score+=1 #lägger till ett poäng för varje äpple som äts

        hx,hy=self.snake.head() # beskriver ormens huvud med x,y koordinater
        if not(0<=hx<self.grid_w and 0<=hy<self.grid_h): #kollar ifall huvudet är utanför spelplanen
            self.draw_game_over()
            self.running=False
        if self.snake.check_colision(): #kollar ifall ormen har kolliderat med sig själv
            self.draw_game_over()
            self.running=False

    def draw(self)->None:
        self.screen.fill((255,255,255)) # fyller bakgrunden med vit färg
        for x,y in self.snake.body:
            rect=(x*self.cell,y*self.cell,self.cell-1,self.cell-1) #omvandlar koordinater till grids, -1 ger lite mellanrum mellan segmenten
            pygame.draw.rect(self.screen,(0,255,12),rect) # ritar ett grönt segment
        fx,fy=self.apple.position # beskriver äpplets position
        rect=(fx*self.cell,fy*self.cell,self.cell-1,self.cell-1) #samma omvandling för äpplet
        pygame.draw.rect(self.screen,(220,60,60),rect) # ritar ett rött äpple
        score_text=self.font.render(f"Score: {self.score}",True,(0,0,0))
        self.screen.blit(score_text,(10,10))
        pygame.display.flip() # skickar allt som ritas till skärmen
    """
    Lade till en välkomst sida
    """
    def draw_welcome(self)->None:
        big_font=pygame.font.SysFont("Arial",40) # definierar fonten för rubriken
        small_font=pygame.font.SysFont("Arial",20) # definierar fonten för underrubriken
        title=big_font.render("Welcome To snake!",True,(0,255,12)) # definierar titeln och ger den färgen grön
        subtitle=small_font.render("Press any movement key to start",True,(100,100,100)) # definierar underrubriken och ger den en grå färg
        self.screen.fill((255,255,255)) # fyller skärmen med svart
        self.screen.blit(title,(225,200)) # skriver ut titeln
        self.screen.blit(subtitle,(245,300)) # skriver ut underrubriken
        pygame.display.flip()

    def draw_game_over(self):
        big_font=pygame.font.SysFont("Arial",40)
        score_font=pygame.font.SysFont("Arial",20)
        title=big_font.render("Game Over!",True,(0,252,12))
        score=score_font.render(f"Score: {self.score}",True,(0,0,0))
        self.screen.fill((255,255,255))
        self.screen.blit(title,(225,200))
        self.screen.blit(score,(245,300))
        pygame.display.flip()
        pygame.time.wait(3000)

    def run(self)->None:
        while self.running:
            self.key_inputs()
            if self.snake.direction==(0,0):
                self.draw_welcome()
                self.clock.tick(30)
            else:
                self.update()
                self.draw()
                self.clock.tick(self.fps)
        pygame.quit()
        print(f"Game Over. Score: {self.score}")
if __name__ == "__main__":
    game=Game()
    game.run()