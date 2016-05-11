from Menu_General import Menu_General
from Menu_Acceuil import Menu_Acceuil
from Menu_Reponse import Menu_Reponse
from Menu_Pose import Menu_Pose
from Menu_End import Menu_End
from Ordre_Menu import Ordre_Menu
#Importation des différents fichiers utile



class Menu_switsh :
    '''Cette class permet de changer de menu'''

    def __init__(self):
        self.menu_list = [] #Liste des différents menus

        self.Menu1 = Menu_Acceuil()
        self.Menu1.setIndice(Ordre_Menu.Acceuil) #Le Menu1 prend l'indice de la class Ordre_Menu
        self.menu_list.append(self.Menu1) #Ajoute l’indice du menu à la liste

        self.Menu2 = Menu_Reponse()
        self.Menu2.setIndice(Ordre_Menu.Reponse) #Le Menu2 prend l'indice de la class Ordre_Menu
        self.menu_list.append(self.Menu2) #Ajoute l’indice du menu à la liste

        self.Menu4 = Menu_Pose()
        self.Menu4.setIndice(Ordre_Menu.Pose) #Le Menu4 prend l'indice de la class Ordre_Menu
        self.menu_list.append(self.Menu4) #Ajoute l’indice du menu à la liste

        self.Menu3 = Menu_End()
        self.Menu3.setIndice(Ordre_Menu.End) #Le Menu3 prend l'indice de la class Ordre_Menu
        self.menu_list.append(self.Menu3) #Ajoute l’indice du menu à la liste

        self.currentMenu = Ordre_Menu.Acceuil #Le menu actuel est l’accueil


    def affichage(self,surface): #Affiche le menu actuel
        self.menu_list[self.currentMenu].affichage(surface)

    def checkEvent(self):
        self.menu_list[self.currentMenu].checkEvent() #Vérifie les évènements du menu actuel
        if self.menu_list[self.currentMenu].getNextChoice() != self.currentMenu : #Si le menu actuel est différent que le menu voulut
            self.currentMenu = self.menu_list[self.currentMenu].getNextChoice() #Le menu actuel devient le menu voulu
            self.menu_list[self.currentMenu].resetChoice() #Le nouveau menu actuel n’a pas de volonté

    def checkEventBis (self,evt):
        self.menu_list[self.currentMenu].checkEventBis(evt)

    def getCurrentMenu (self): #Fonction qui retourne le menu actuel
        return self.currentMenu


    def setEnd(self): #Fonction qui rend le menu de fin actuel
        self.currentMenu = Ordre_Menu.End

    def checkDataToSend (self,dt):
        self.menu_list[self.currentMenu].checkDataToSend(dt)
