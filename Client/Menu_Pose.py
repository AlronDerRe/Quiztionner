from Bouton import Bouton
from Menu_General import Menu_General
from Ordre_Menu import Ordre_Menu
from Text import Text
from TextBar import TextBar



class Menu_Pose(Menu_General): #Classe fille de Menu_General

    def __init__(self):
        self.t1 = TextBar(30,30,'', 'image/Bar1.png')
        self.t2 = TextBar(30,190,'', 'image/Bar2.png')
        self.t3 = TextBar(30,350,'', 'image/Bar3.png')
        self.b1 = Bouton('image/BRR.png',100,515)
        self.b2 = Bouton('image/BPV.png',500,515)
        #initialisation des barres de texte et des boutons

    def checkEvent(self): #Vérification des évènements utilisateurs et des requête de changement de menu.
        self.t1.checkEvent()
        self.t2.checkEvent()
        self.t3.checkEvent()
        self.b1.checkEvent()
        self.b2.checkEvent()

        if self.b1.isClicked() == True: #Si le bouton a été cliqué on reset les barres de texte.
            self.t1.resetText()
            self.t2.resetText()
            self.t3.resetText()
            self.nextChoiceMenu = Ordre_Menu.Acceuil #Alors le menu accueil est choisi


    def checkEventBis(self,evt): #gestion des évènements de types entré clavier (ne sont pas géré de la même manière que les clics, ce qui explique la fonctin checkEventBis).
        self.t1.checkEventBis(evt)
        self.t2.checkEventBis(evt)
        self.t3.checkEventBis(evt)

    def checkDataToSend(self,dt): #Vérification de si il faut oui ou non envoyer des données au serveur depuis ce menu
        if self.b2.isClicked() == True:
            if self.t1.getText() != '' and self.t2.getText() != '' and self.t3.getText() != '' :
                a = '$0000000000newQ/' + str(self.t1.getText()) + '/' + str(self.t2.getText()) + '/' + str(self.t3.getText()) + '%' #Encodage
                dt.addDataToSend(a) 

                self.t1.resetText() #i on en envoi alors on reset les textBar
                self.t2.resetText()
                self.t3.resetText()

    def affichage(self,surface): #affichage du menu
        self.t1.display(surface)
        self.t2.display(surface)
        self.t3.display(surface)
        self.b2.display(surface)
        self.b1.display(surface)
