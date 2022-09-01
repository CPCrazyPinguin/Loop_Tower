
import zusatz
import pygame
import map

class Level():
    def __init__(self):
        self.map = map.Map(zusatz.Vector(8, 3), 6, 6)
    
    def draw(self,screen):
        #pygame.draw.rect(screen, (100,100,200), (100,100,100,100),0)
        self.map.draw(screen)
        
    def rescale(self, groesse):
        self.map.rescale(groesse)