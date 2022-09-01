import zusatz
import pygame

class Startgame():
    def __init__(self):
        print("starting game")
        
        self.finish = False
        
        self.text = [0]*2
        
        self.start_button = zusatz.Button_text((200,10,10), (0,100,0), zusatz.Text(zusatz.Vector(0.5, 0.6), 0.05, " START "))
        
        self.text[0] = zusatz.Text(zusatz.Vector(0.5, 0.3), 0.08, "Loop Tower")
        self.text[1] = zusatz.Text(zusatz.Vector(0.5, 0.4), 0.03, "by V0LT0RN & BloodyMary & CrazyPinguin_")
        
    def draw(self,screen,groesse):
        
        self.start_button.draw_center(screen, groesse)
        
        self.text[0].draw_center(screen, groesse)
        self.text[1].draw_center(screen, groesse)