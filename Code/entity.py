
import zusatz
import pygame

class Entity():
    def __init__(self, orientation, typ, pos, size):
        self.orientation = orientation
        self.moves = 0
        #self.bild = pygame.image.load(os.path.join("Bilder", "" + typ + "png"))
        
        print("Lade Config_data für " + typ + " ///////////////////////")
        self.data = open(os.path.join("config","" + typ + ".txt")).read()
        self.data = self.data.replace("\n","")
        self.data = self.data.replace("\t","")
        self.data = self.data.replace(" ","")
        self.data = self.data.split(";")
        for i in range(len(self.data)):
            self.data[i] = self.data[i].split("=")
            if self.data[i][1][0] == "[":
                self.data[i][1] = self.data[i][1].replace("[","").replace("]","")
                self.data[i][1] = self.data[i][1].split(",")
                
        self.pos = pos
        self.draw_pos = pos
        self.size = zusatz.Vector(0.01, 0.01) #self.data
        self.draw_size = self.size
        
    def rescale(self,groesse):
        self.draw_pos = zusatz.Vector(groesse.x * self.pos.x, groesse.y * self.pos.y)
        self.draw_size = zusatz.Vector(groesse.x * self.size.x, groesse.y * self.size.y)
                
    def draw(self,screen, groesse):
        screen.blit(pygame.transform.scale(self.bild,(self.draw_size.x,self.draw_size.y)),(self.draw_pos.x,self.draw_pos.y))
    