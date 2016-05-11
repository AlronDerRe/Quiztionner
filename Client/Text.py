import pygame

class Text:

    def __init__(self,posX,posY,t,p):
        self.posX0 = posX
        self.posY0 = posY
        self.posX1 = posX + 6
        self.posY1 = posY + 6
        self.t = t
        self.font = pygame.font.Font('MyriadPro.otf',p)
        self.couleur = (236,240,241)
        self.block = self.font.render(self.t, True, (self.couleur))
        self.textpos = self.block.get_rect()
        self.textpos.centerx = self.posX0
        self.textpos.centery = self.posY0

    def checkEvent(self, Bouton):
        if Bouton.isPushed() == True :
            self.textpos.centerx = self.posX1
            self.textpos.centery = self.posY1
        else :
            self.textpos.centerx = self.posX0
            self.textpos.centery = self.posY0

    def getText(self):
        return self.t

    def display(self,surface):
        surface.blit(self.block,self.textpos)

    def getSize(self):
        return self.font.size(self.t)[0]

    def changeText(self, txt):
        self.t = txt
        self.block = self.font.render(self.t, True, (self.couleur))
        self.textpos = self.block.get_rect()
        self.textpos.centerx = self.posX0
        self.textpos.centery = self.posY0
