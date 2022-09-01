
import pygame

#Klasse für Positionen
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def multi(self,var):
        self.x = self.x*var
        self.y = self.y*var
    def round(self,var):
        self.x = round(self.x,var)
        self.y = round(self.y, var)

def toggle(var):
    if var:
        return False
    else:
        return True

class Button():
    def __init__(self,b_activ):
        self.b_activ = b_activ
        self.colision = 0
    def draw(self,screen,pos,width,height):
        screen.blit(pyg.transform.scale(self.b_activ,(width,height)),(pos.x,pos.y))
        self.colision = pyg.draw.rect(screen,(0,0,0),(pos.x,pos.y,width,height),1)
    def update(self,mouspos,pressed1):
        if self.colision.collidepoint(mouspos)& pressed1==1:
            return True
        else:
            return False
        
class Text():
    def __init__(self,pos,text_groesse,text):
        self.pos = pos
        self.text = text
        self.text_groesse = text_groesse
        self.size = Vector(1, 1)
        self.center = Vector(1, 1)
        
    #@param pos, mittelpunkt des Textfeldes
    def draw_center(self,screen,groesse):
        self.myfont = pygame.font.SysFont("arial",int(groesse.y*self.text_groesse))
        self.label = self.myfont.render(self.text, 1, (255,255,255))
        self.size.x, self.size.y = self.myfont.size(self.text)
        self.center = Vector((groesse.x * self.pos.x) - (self.size.x / 2), (groesse.y * self.pos.y) - (self.size.y / 2))
        screen.blit(self.label,([self.center.x,self.center.y]))
    
    #@param pos, linke obere Ecke des Feldes
    def draw_absolut(self,screen,groesse):
        self.myfont = pygame.font.SysFont("arial",int(groesse.y*self.text_groesse))
        self.label = self.myfont.render(self.text, 1, (255,255,255))
        self.size.x, self.size.y = self.myfont.size(self.text)
        screen.blit(self.label,([groesse.x*self.pos.x,groesse.y*self.pos.y]))
        
class Button_text():
    def __init__(self,fill_color, rand_color, text):
        self.fill_color = fill_color
        self.rand_color = rand_color
        self.text = text
        self.colision = 0
        
    def draw_center(self,screen,groesse):
        self.text.draw_center(screen,groesse)
        pygame.draw.rect(screen,self.fill_color,(self.text.center.x, self.text.center.y, self.text.size.x, self.text.size.y),0)
        self.colision = pygame.draw.rect(screen,self.rand_color,(self.text.center.x, self.text.center.y, self.text.size.x, self.text.size.y),2)
        self.text.draw_center(screen,groesse)
        
    def draw_absolut(self,screen,groesse):
        self.text.draw_center(screen,groesse)
        pygame.draw.rect(screen,self.fill_color,(self.text.pos.x*groesse.x, self.text.pos.y*groesse.y, self.text.size.x, self.text.size.y),0)
        self.colision = pygame.draw.rect(screen,self.rand_color,(self.text.pos.x*groesse.x, self.text.pos.y*groesse.y, self.text.size.x, self.text.size.y),2)
        self.text.draw_absolut(screen,groesse)
        
    def update(self,mouspos,pressed1):
        if self.colision.collidepoint(mouspos)& pressed1==1:
            return True
        else:
            return False