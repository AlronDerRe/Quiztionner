from Bouton import Bouton
from Menu_General import Menu_General
from Ordre_Menu import Ordre_Menu
from Text import Text
from PopupScore import PopupScore
#Importation des différents fichiers utile



class Menu_Reponse(Menu_General):
    '''Cette class correspond au caractéristique du Menu_Reponse'''

    def __init__(self):
        self.b1 = Bouton('image/ECRAN.png',30,30)
        self.b2 = Bouton('image/BR1.png',45,225)
        self.b3 = Bouton('image/BR2.png',45,370)
        self.b4 = Bouton('image/BRR.png',100,515)
        self.t1 = Text(30 + 740/2,30 + 165/2,"",35)
        self.t2 = Text(45 + 710/2,225 + 115/2,"",32)
        self.t3 = Text(45 + 710/2,370 + 115/2,"",32)
        self.popupScore = PopupScore()
        self.needQ = True
        self.id = 0
        self.openPopup = False

        #Image et coordonné de chaque bouton du menu

    def checkEvent(self):
        if self.popupScore.getIsActive() == False :
            self.b1.checkEvent()
            self.b2.checkEvent()
            self.b3.checkEvent()
            self.b4.checkEvent()

            #Fonction qui vérifie les évènements de chacun des boutons

            if self.b4.isClicked() == True: #Si le bouton a été cliqué
                self.nextChoiceMenu = Ordre_Menu.Acceuil #Alors le menu accueil est choisi
                self.needQ = True

            if self.b2.isClicked() == True :
                self.needQ = True

            if self.b3.isClicked() == True :
                self.needQ = True


            self.t2.checkEvent(self.b2)
            self.t3.checkEvent(self.b3)

            if self.openPopup == True:
                self.popupScore.setActive(True)
                self.openPopup = False
        else :
            self.popupScore.checkEvent()

    def checkEventBis(self,evt):
        1+1

    def checkDataToSend(self,dt):
        if self.needQ == True :
            dt.addDataToSend('$0000000000QuestionAsk/a%')
            self.needQ = False
        if self.b2.isClicked() == True :
            dt.addDataToSend('$0000000000Answer/%s/%s' % (self.id , '1%') )
            dt.addDataToSend('$0000000000Score/' + str(self.id) + '%' )
            self.openPopup=True
        if self.b3.isClicked() == True :
            dt.addDataToSend('$0000000000Answer/%s/%s' % (self.id , '2%') )
            dt.addDataToSend('$0000000000Score/' + str(self.id) + '%' )
            self.openPopup=True


    def affichage(self,surface): #Fonction qui affiche les boutons
        self.b2.display(surface)
        self.b1.display(surface)
        self.b3.display(surface)
        self.b4.display(surface)
        self.t1.display(surface)
        self.t2.display(surface)
        self.t3.display(surface)
        if self.popupScore.getIsActive() == True :
            self.popupScore.display(surface)
