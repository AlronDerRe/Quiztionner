import pygame




class Bouton:
    '''Cette class correspond aux différents évènements du bouton'''

    def __init__(self, chemin, posX, posY):
        self.list = [] #Liste des etats du bouton
        self.posX = posX #Position X du bouton
        self.posY = posY #Position Y du bouton
        self.Texture = pygame.image.load(chemin).convert_alpha() #Chargement de l’image du bouton
        (self.sizeX,self.sizeY) = self.Texture.get_size() #Taille de limage
        self.imgNeutre = self.Texture.subsurface((pygame.Rect(0, 0, self.sizeX/3, self.sizeY))) #Partie de l’image correspondant à la phase neutre du bouton
        self.imgAppuye = self.Texture.subsurface((pygame.Rect(self.sizeX/3, 0, self.sizeX/3, self.sizeY))) #Partie de l’image correspondant à la phase appuyé du bouton
        self.imgVisualise = self.Texture.subsurface((pygame.Rect(self.sizeX/3*2, 0, self.sizeX/3, self.sizeY))) #Partie de l’image correspondant à la phase visualisé du bouton
        self.list.append(self.imgNeutre) #Ajoute l’image dans la liste
        self.list.append(self.imgVisualise) #Ajoute l’image dans la liste
        self.list.append(self.imgAppuye) #Ajoute l’image dans la liste
        self.currentButton = 0 #Etat actuel du bouton
        self.clic = 0 #Etat du clic
        self.relache = 0 #Etat du relachement
        self.focus = False

    def checkEvent(self): #Ici on actualise l'état du bouton
        (Mx,My) = pygame.mouse.get_pos() #Coordonné de la position de la souri
        buttonpress=pygame.mouse.get_pressed() #Bouton de la souri appuyé
        if self.relache == 1:
            self.relache = 0

        if Mx > self.posX and Mx < self.posX + self.sizeX/3 and My > self.posY and My < self.posY + self.sizeY : #Si la souris est dans le bouton
            self.currentButton = 2 #Alors le bouton est visualisé
            if pygame.mouse.get_pressed()==(1,0,0): #Si on clique avec le clic gauche
                self.currentButton = 1 #Alors le bouton est appuyé
                self.clic = 1
                self.focus = True
            else :
                if self.clic == 1 :
                    self.relache = 1
                else :
                    self.relache = 0
                self.clic = 0
  

        else:
            if pygame.mouse.get_pressed()==(1,0,0):
                self.focus = False
            self.currentButton = 0 #Sinon le bouton est neutre
            self.clic = 0
            self.relache = 0




    def isClicked(self): #Fonction qui permet de savoir si ça a été cliqué
        if self.relache == 1:
            return True
        else :
            return False

    def hasFocus(self):
        return self.focus

    def isPushed(self):
        if self.currentButton == 1:
            return True
        else :
            return False

    def getBoutonSizeX(self):
        return self.sizeX/3

    def getBoutonSizeY(self):
        return self.sizeY





    def display(self,surface): #Fonction qui affiche le boutons à l’aide de son image et de ses coordonné
        surface.blit(self.list[self.currentButton], ( self.posX,self.posY))
