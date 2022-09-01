#!/usr/bin/python
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time
import zusatz
import sys
import os

import startgame
import controller
import level


class Programm:
    def __init__(self):
        #Pygame inizialisieren
        pygame.init()
        #groessen setzten
        self.width = 1000
        self.height = 500
        self.oldw = 1000
        self.oldh = 500
        self.bild_groesse = zusatz.Vector(self.width, self.height)
        #Fenster erstellen
        self.screen = pygame.display.set_mode((1000,500),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        #Name des Fensters setzen
        pygame.display.set_caption("Spiel by CrazyPinguin_ und Co.")
        #Maus un/sichtbar machen
        pygame.mouse.set_visible(1)
        #interne Uhr einstellen
        self.clock = pygame.time.Clock()
        #Variablen
        self.fps = 60

        #Lade Config
        print("Lade Config ///////////////////////")
        datei = open(os.path.join("config","Config.txt")).read()
        datei = datei.replace("\n","")
        datei = datei.replace("\t","")
        datei = datei.replace(" ","")
        datei = datei.split(";")
        for i in range(len(datei)):
            datei[i] = datei[i].split("=")

        datei[3][1] = datei[3][1].replace("[","")
        datei[3][1] = datei[3][1].replace("]","")
        datei[3][1] = datei[3][1].split(",")

        datei[4][1] = datei[4][1].replace("[","")
        datei[4][1] = datei[4][1].replace("]","")
        datei[4][1] = datei[4][1].replace("(","")
        datei[4][1] = datei[4][1].replace(")","")
        datei[4][1] = datei[4][1].replace("%","")
        datei[4][1] = datei[4][1].split(",")
        for i in range(len(datei[4][1])):
            datei[4][1][i] = datei[4][1][i].split(":")

        self.datei = datei
        #Klassen

        self.Startgame = startgame.Startgame()
        self.Controller = controller.Controller()
        self.Level = level.Level()

        #Klassenbestimmung

    def play(self):
        #Spielstart
        print("\nSpielstart")
        while True:
            #Durchläufe auf fps, frames per second, setzen
            self.clock.tick(self.fps)
            #Hintergrundfarbe
            self.screen.fill((10,200,100))
            if self.Startgame.finish:
                self.Level.draw(self.screen)
            else:
                self.Startgame.draw(self.screen, self.bild_groesse)


            #Events Tasten/Mauseingaben
            #Mausposition
            mouspos = pygame.mouse.get_pos()
            #Mausklick
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            #setzt die gedrueckten keys auf True
            keys = pygame.key.get_pressed()
            #Abfrage alle Events in Pygame
            for event in pygame.event.get():
                #Beenden event
                if event.type == pygame.QUIT:
                    #Beende Spiel und verlasse Programm
                    spielschleife = False
                    sys.exit()
                    exit()
                #Tastendruck
                if event.type == pygame.KEYDOWN:
                    #ESC Taste
                    if self.Startgame.finish:
                        self.Startgame.finish = False
                    else:
                        if event.key == pygame.K_ESCAPE:
                            #Erzeuge Beenden event
                            pygame.event.post(pygame.event.Event(pygame.QUIT))
                #Screen rekonfiguration, Fullscreen
                if event.type == VIDEORESIZE:
                    #setze Bild auf Bilschrimgroesse
                    self.screen = pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                    #aktualisiere Bild
                    pygame.display.flip()
                    #speichere originalgroesse
                    self.oldw, self.oldh = self.width, self.height
                    #speichere aktuelle groesse
                    self.width, self.height = pygame.display.get_surface().get_size()

                    #Karte rescalieren
                    self.rescale()
                    #Karte.rescale(bild_groesse)

                #Unsere Events
                self.Controller.event_handler(self, event, mouspos, pressed1, pressed2, pressed3, self.Startgame, self.Level)

            #aktualisiere das Bild
            pygame.display.flip()

    def rescale(self):
        self.bild_groesse = zusatz.Vector(self.width, self.height)
        self.Level.rescale(self.bild_groesse)


#rufe das Spiel auf
while True:
    print("\n\nNeuer Anfang\n")
    Programm = Programm()
    Programm.play()
    
