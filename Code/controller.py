import zusatz


class Controller():
    #Konstruktor von Controller
    def __init__(self):
        print("Steuerung online")
        self.mouspos = (0,0)
        self.mous_hold = False
        
    def event_handler(self,Programm, event,mouspos, pressed1, pressed2, pressed3, startgame, level):
        if startgame.start_button.update(mouspos, pressed1):
            startgame.finish = True
        if startgame.finish:
            if pressed3:
                #nach rescale auslagern, da nur nach neuer Größe neu berechnet werden muss
                #size = self.felder[self.startpos.x+self.startpos.y*self.max_y].draw_size
                #a = (self.position.x+pos.x)*0.5*size.x
                #b = -self.pos.y*0.5*size.y
                #c = self.pos.x*0.25*size.x
                #d = self.draw_pos.y*0.25*size.y
                #tile_x = mouspos.x
                level.map.zoom(2)
                Programm.rescale()
            if pressed2:
                level.map.zoom(0.5)
                Programm.rescale()


            if pressed1 and not self.mous_hold:
                self.mous_hold = True
                self.mouspos = mouspos

            if self.mous_hold and not pressed1:
                self.mous_hold = False

            if self.mous_hold and pressed1:
                offset = zusatz.Vector((mouspos[0]-self.mouspos[0])/Programm.width,
                                       (mouspos[1]-self.mouspos[1])/Programm.height)
                offset.round(2)
                offset.multi(-2)
                level.map.move_map(offset)
                Programm.rescale()



            