class Menu_General:
    '''Cette classe est la superclasse de toutes les autre classes des menus'''
    def __init__(self):
        self.nextChoiceMenu #Variable du choix du prochain menu
        self.indiceFix #Sauvegarde de l’indice

    def getNextChoice (self): #Fonction qui retourne le choix du menu
        return self.nextChoiceMenu

    def setIndice(self,indice): #Fonction qui initialise les indices des menus
        self.nextChoiceMenu = indice
        self.indiceFix = indice

    def resetChoice (self): #Fonction qui réinitialise les indices
        self.nextChoiceMenu = self.indiceFix
