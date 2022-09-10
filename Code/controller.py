import zusatz


class Controller():
    #Konstruktor von Controller
    def __init__(self):
        print("Steuerung online")
        self.mouspos = (0,0)
        self.mous_hold = False

        #mous to field Coordinats
        self.size = 0
        self.iso_matrix = zusatz.Matrix(0.5, -0.5, 0.25, 0.25)
        self.mous_matrix = self.iso_matrix
        
    def event_handler(self,Programm, event,mouspos, pressed1, pressed2, pressed3, startgame, level):
        if startgame.start_button.update(mouspos, pressed1):
            startgame.finish = True
        if startgame.finish:
            if pressed1:
                mous = zusatz.Vector(mouspos[0], mouspos[1])
                mous.sub(self.size)
                v = self.mous_matrix.get_vector_multi(mous)
                v.round(1)
                print("x: " + str(v.x) + "y: " + str(v.y))
                v.round(0)
                if Programm.Level.map.is_in_field(v):
                    print("x: " + str(v.x) + "y: " + str(v.y))
                    Programm.Level.map.change_field(v)
                    Programm.rescale()

            ##    level.map.zoom(2)
            ##    Programm.rescale()
            ##if pressed2:
            ##    level.map.zoom(0.5)
            ##    Programm.rescale()


            if pressed2 and not self.mous_hold:
                self.mous_hold = True
                self.mouspos = mouspos

            if self.mous_hold and not pressed2:
                self.mous_hold = False

            if self.mous_hold and pressed2:
                offset = zusatz.Vector((mouspos[0]-self.mouspos[0])/Programm.width,
                                       (mouspos[1]-self.mouspos[1])/Programm.height)
                offset.round(2)
                offset.multi(-0.5)
                offset.round(2)
                level.map.move_map(offset)
                Programm.rescale()




            