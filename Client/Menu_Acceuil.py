from Bouton import Bouton
from Menu_General import Menu_General
from Ordre_Menu import Ordre_Menu
#Importation des différents fichiers utile



class Menu_Acceuil(Menu_General):
    '''Cette class correspond au caractéristique du Menu_Acceuil'''

    def __init__(self):
        self.b1 = Bouton('image/BMR.png',90,235)
        self.b2 = Bouton('image/BMP.png',90,375)
        self.b3 = Bouton('image/BMQ.png',715,515)
        self.logo = Bouton('image/logo.png',100,59)
        #Image et coordonné de chaque bouton du menu


    def checkEvent(self):
        self.b1.checkEvent()
        self.b2.checkEvent()
        self.b3.checkEvent()
        #Fonction qui vérifie les évènements de chacun des boutons

        if self.b1.isClicked() == True: #Si le bouton a été cliqué
            self.nextChoiceMenu = Ordre_Menu.Reponse #Alors le menu réponse est choisi

        elif self.b2.isClicked() == True: #Si le bouton a été cliqué
            self.nextChoiceMenu = Ordre_Menu.Pose #Alors le menu pose est choisi

        elif self.b3.isClicked() == True: #Si le bouton a été cliqué
            self.nextChoiceMenu = Ordre_Menu.End #Alors le menu de fin est choisi

    def checkEventBis(self,evt):
        1+1

    def checkDataToSend(self,dt):
        1+1



    def affichage(self,surface): #Fonction qui affiche les boutons
        self.b2.display(surface)
        self.b1.display(surface)
        self.b3.display(surface)
        self.logo.display(surface)
