import pygame
from Text import Text
from Bouton import Bouton
from pygame.locals import *


class TextBar:

    def __init__(self,posX,posY,t, chemin):
        self.posX = posX
        self.posY = posY
        self.text = t
        self.b = Bouton(chemin,posX,posY)
        self.t = Text(posX+self.b.getBoutonSizeX()/2,posY+self.b.getBoutonSizeY()/2, self.text,35)
        self.Write = False


    def checkEvent(self):
        self.b.checkEvent()
        self.Write = self.b.hasFocus()

    def checkEventBis(self,evt) :
        if self.Write == True :
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha() and evt.unicode != '$' and evt.unicode != '%':
                    self.text += evt.unicode
                elif evt.unicode.isdigit():
                    self.text += evt.unicode
                elif evt.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                elif evt.key == K_SPACE:
                    self.text += " "
                elif evt.unicode.encode('utf-8') and evt.unicode != '$':
                    self.text += evt.unicode
                if self.t.getSize() > 660 :
                    self.text = self.text[:-1]


                self.t = Text(self.posX+self.b.getBoutonSizeX()/2,self.posY+self.b.getBoutonSizeY()/2, self.text,35)

    def resetText(self):
        self.text = ''
        self.t = Text(self.posX+self.b.getBoutonSizeX()/2,self.posY+self.b.getBoutonSizeY()/2, self.text,35)

    def getText(self):
        return self.text

    def display(self, surface):
        self.b.display(surface)
        self.t.display(surface)
