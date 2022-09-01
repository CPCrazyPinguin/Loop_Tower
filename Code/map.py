
import field
import zusatz

class Map():
    def __init__(self,position,max_x,max_y):
        self.position = zusatz.Vector(0, 0)
        self.startpos = zusatz.Vector(1, 1)
        self.endpos = zusatz.Vector(5, 5)
        self.max_x = max_x
        self.max_y = max_y

        self.mouspos = (0,0)
        
        self.felder = [0]*(max_x*(max_y+1))
        
        self.felder[self.startpos.x+self.startpos.y*max_y] = field.Start_Field("startfield", self.startpos,0, 100, "s")
        self.felder[self.endpos.x+self.endpos.y*max_y] = field.End_Field("endfield", self.endpos,0, "n")

        pos = zusatz.Vector(0, 0)

        self.felder[pos.x+pos.y*max_y] = field.End_Field("endfield", pos ,0, "n")
        self.felder[1+0*max_y] = field.End_Field("endfield", zusatz.Vector(1, 0), 0, "n")
        self.felder[2+0*max_y] = field.End_Field("endfield", zusatz.Vector(2, 0), 0, "n")
        self.felder[3+0*max_y] = field.End_Field("endfield", zusatz.Vector(3, 0), 0, "n")
        self.felder[4+0*max_y] = field.End_Field("endfield", zusatz.Vector(4, 0), 0, "n")
        self.felder[5+0*max_y] = field.End_Field("endfield", zusatz.Vector(5, 0), 0, "n")
        self.felder[6+0*max_y] = field.End_Field("endfield", zusatz.Vector(6, 0), 0, "n")
        self.felder[0+1*max_y] = field.End_Field("endfield", zusatz.Vector(0, 1), 0, "n")
        self.felder[0+2*max_y] = field.End_Field("endfield", zusatz.Vector(0, 2), 0, "n")
        self.felder[0+3*max_y] = field.End_Field("endfield", zusatz.Vector(0, 3), 0, "n")
        self.felder[0+4*max_y] = field.End_Field("endfield", zusatz.Vector(0, 4), 0, "n")
        self.felder[0+5*max_y] = field.End_Field("endfield", zusatz.Vector(0, 5), 0, "n")
        
        
        #Spielfeld
        temp = []
        for i in range(0,len(self.felder)):
            if i % 6 == 0:
                #print(temp)
                temp = []
            temp.append(self.felder[i])
        #print(temp)

        self.move_map(position)
        
        
    def set_Path_Field(self,typ,pos):
        #pos = x-index,y-index in felderliste
        next_field = pos
        if typ[-1] == "e":
            next_field.x += 1
        elif typ[-1] == "w":
            next_field.x -= 1
        elif typ[-1] == "s":
            next_field.y += 1
        else:
            next_field.y -= 1
        
        print("next_field")
        if str(type(self.felder[next_field.x+next_field.y*6])) == "<class 'field.Path_Field'>":
            print("type!")
            self.felder[pos.x+pos.y*6] == field.Path_Field(typ,pos, next_field)
            return True
        elif self.felder[next_field.x+next_field.y*6] == 0:
            return False
        
    def rescale(self,groesse):
        for i in range(0, len(self.felder)):
            if self.felder[i] != 0:
                self.felder[i].rescale(groesse)

    def zoom(self, zoom):
        for i in range(0, len(self.felder)):
            if self.felder[i] != 0:
                self.felder[i].size.multi(zoom)

    def move_map(self, offset):
        print("//move Map")
        self.position.x += offset.x
        self.position.y += offset.y
        for i in range(0, len(self.felder)):
            if self.felder[i] != 0:
                self.felder[i].offset = self.position


    def draw(self,screen):
        for i in range(0,len(self.felder)):
            if self.felder[i] != 0:
                self.felder[i].draw(screen)
