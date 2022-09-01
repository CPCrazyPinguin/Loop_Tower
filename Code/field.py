
from ctypes.wintypes import HPALETTE
import pygame
import os
import zusatz

class Field():
    def __init__(self, typ, pos, next_field):
        self.bild = pygame.image.load(os.path.join("Bilder", "iso_feld.png")) #"" + typ + ".png"))
        self.pos = pos  
        self.size = zusatz.Vector(0.1, 0.2)
        self.draw_size = zusatz.Vector(int(5), int(5))
        self.draw_pos = zusatz.Vector(self.pos.x - self.pos.y, self.pos.x * 0.5 + self.pos.y * 0.5)
        self.center_pos = self.pos
        self.next_field = next_field #int index in felderliste in Karte
        self.offset = zusatz.Vector(0, 0)

        print("Lade Config_data für " + typ + " ///////////////////////")
        #self.data = open(os.path.join("config","" + typ + ".txt")).read()
        #self.data = self.data.replace("\n","")
        #self.data = self.data.replace("\t","")
        #self.data = self.data.replace(" ","")
        #self.data = self.data.split(";")
        #for i in range(len(self.data)):
        #    self.data[i] = self.data[i].split("=")
        #    if self.data[i][1][0] == "[":
        #        self.data[i][1] = self.data[i][1].replace("[","").replace("]","")
        #        self.data[i][1] = self.data[i][1].split(",")
        
    def draw(self,screen):
        screen.blit(pygame.transform.scale(self.bild,(self.draw_size.x,self.draw_size.y)),(self.draw_pos.x,self.draw_pos.y))
        
        
    def rescale(self,groesse):
        self.draw_size = zusatz.Vector(int(groesse.x * self.size.x), int(groesse.y * self.size.y))
        self.draw_pos = zusatz.Vector(self.pos.x + self.offset.x, self.pos.y + self.offset.y)
        #self.draw_pos = self.pos
        self.draw_pos = zusatz.Vector(self.draw_pos.x * 0.5 * self.draw_size.x - self.pos.y * 0.5 * self.draw_size.y, self.pos.x * 0.25 * self.draw_size.x + self.draw_pos.y * 0.25 * self.draw_size.y)
        #self.draw_pos = zusatz.Position(self.draw_pos.x * self.draw_size.x, self.draw_pos.y * self.draw_size.y)
        self.center_pos = zusatz.Vector(self.draw_pos.x - self.size.x / 2, self.draw_pos.y - self.size.y / 2)
        
        #print(self.draw_pos.x)
        #print(self.draw_pos.y)
        #print(self.draw_size.x)
        #print(self.draw_size.y)
    
        
class Path_Field(Field):
    def __init__(self, typ, pos, next_field):
        super().__init__(typ, pos, next_field)
        
        #self.move_in = self.data[0][1]
        #self.move_out = self.data[1][1]
        
        self.Entitys = []
        
    def draw(self,screen):
        screen.blit(pygame.transform.scale(self.bild,(self.draw_size.x,self.draw_size.y)),(self.draw_pos.x,self.draw_pos.y))
        
        #for i in self.Entitys:
        #    i.draw(screen, groesse)
                
        
    def update(self,felder):
        for i in range(0,len(self.Entitys)):
            if self.Entitys[i].moves == 10: #hälfte maximal moves
                if self.Entitys[i].orientation == self.move_out:
                    self.Entitys[i].moves += 1
                else:
                    self.Entitys[i].orientation = self.move_out
            elif self.Entitys[i].moves == 20: #maximal moves
                felder[self.next_field.x][self.next_field.y].Entitys.append(self.Entitys.pop(i))
            else:
                self.Entitys[i].moves += 1
            
            if self.Entitys[i].orientation == "n":
                self.Entitys[i].pos = self.center_pos + self.size.x*(10 - self.Entitys[i].moves)
            elif self.Entitys[i].orientation == "s":
                self.Entitys[i].pos = self.center_pos + self.size.x*(self.Entitys[i].moves - 10)
            elif self.Entitys[i].orientation == "w":
                self.Entitys[i].pos = self.center_pos + self.size.y*(10 - self.Entitys[i].moves)
            elif self.Entitys[i].orientation == "e":
                self.Entitys[i].pos = self.center_pos + self.size.y*(self.Entitys[i].moves - 10)

class Start_Field(Field):
    def __init__(self, typ, pos, next_field, hp, move_in):
        super().__init__("" + typ + "-" + move_in, pos, next_field)
        self.hp = hp
        self.move_in = move_in
        
class End_Field(Field):
    def __init__(self, typ, pos, next_field, move_out):
        super().__init__("" + typ + "-" + move_out, pos, next_field)
        self.move_out = move_out
        