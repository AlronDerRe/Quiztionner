import pygame
from Text import Text
from Bouton import Bouton
from pygame.locals import *


class TextBar:

    def __init__(self,posX,posY,t, chemin): #Initialisation des composantes.
        self.posX = posX
        self.posY = posY
        self.text = t
        self.b = Bouton(chemin,posX,posY)
        self.t = Text(posX+self.b.getBoutonSizeX()/2,posY+self.b.getBoutonSizeY()/2, self.text,35)
        self.Write = False


    def checkEvent(self): #On vérifie si la barre est sélectionnée(via un bouton), si on pourra écrire dedans. 
        self.b.checkEvent()
        self.Write = self.b.hasFocus()

    def checkEventBis(self,evt) : #Récupération des entrées clavier dans le cadre d'une saisie de texte.
        if self.Write == True :
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha() and evt.unicode != '$' and evt.unicode != '%': #On ne permet pas d'écrire les signes $ et % du fait de leur utilisation dans la syntaxe réseau
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


                self.t = Text(self.posX+self.b.getBoutonSizeX()/2,self.posY+self.b.getBoutonSizeY()/2, self.text,35) #Replacement du texte après ajout/retrait de lettres

    def resetText(self): #Remise à 0 de la textBar
        self.text = ''
        self.t = Text(self.posX+self.b.getBoutonSizeX()/2,self.posY+self.b.getBoutonSizeY()/2, self.text,35)

    def getText(self): #getter
        return self.text

    def display(self, surface): #Affichage
        self.b.display(surface)
        self.t.display(surface)
