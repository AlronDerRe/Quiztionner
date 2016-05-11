import pygame
from Text import Text

class PopupScore():

    def __init__(self):
        self.list = []
        self.Texture = pygame.image.load('image/popup.png').convert_alpha()
        self.active = False
        self.clic = False
        self.ts = Text(400,170,"Statistiques",25)
        self.stat1 = 50
        self.stat2 = 50
        self.colorRect1 = (255, 255, 255)
        self.colorRect2 = (255, 255, 255)


    def checkEvent(self):
        (Mx,My) = pygame.mouse.get_pos()
        buttonpress=pygame.mouse.get_pressed()
        if Mx > 600 or Mx < 200 or My < 130 or My > 470 :
            if pygame.mouse.get_pressed()==(1,0,0):
                    self.clic = True
            else :
                if self.clic == True :
                    self.active = False
                    self.stat1 = 50
                    self.stat2 = 50
                    self.colorRect1 = (255, 255, 255)
                    self.colorRect2 = (255, 255, 255)
                self.clic = False


    def setActive(self,a):
        self.active = a

    def getIsActive(self):
        return self.active

    def setStat(self,r1,r2):
        self.stat1 = 100*int(r1)/(int(r1)+int(r2))
        self.stat2 = 100*int(r2)/(int(r1)+int(r2))
        print (str(self.stat1) + '   ' + str(self.stat2))
        self.colorRect1 = (155,89,182)
        self.colorRect2 = (230,126,34)

    def display(self,surface):
        surface.blit(self.Texture, ( 0,0))
        self.ts.display(surface)
        pygame.draw.rect(surface,(self.colorRect1), [220,250,360,80])
        pygame.draw.rect(surface,(self.colorRect2), [220,250,360*self.stat1*0.01,80])
