import pygame
from Bouton import Bouton
from Menu_General import Menu_General
from Menu_Acceuil import Menu_Acceuil
from Menu_Reponse import Menu_Reponse
from Menu_switsh import Menu_switsh
from Ordre_Menu import Ordre_Menu
from DataHandler import DataHandler
from ClientUpdater import ClientUpdater
from client import Client
#Importation des différents fichiers utile et du module pygame

class GameLoop : #Boucle principale de jeu
    ''''''

    def __init__(self):
        #self.dt = DataReceiver()

        self.surface = pygame.display.set_mode((800,600)) #Définition de la fenêtre

        self.switch = Menu_switsh() #Définition du gestionnaire de menu
        self.client = Client() #Définition du client pour les transmissions réseau
        self.DH = DataHandler() #Définition du DataHandler pour traiter les messages reçus.
        self.clientUpdater = ClientUpdater(self.DH,self.client) #Défintion du ClientUpdater qui modifiera les valeurs des variables en fonction des données reçues

        self.fond =(52,73,94) #Couleur du fond du programme

        self.clock = pygame.time.Clock() #Timer pour limiter le framerate


    def run(self):
        Q = False
        while not Q: #Boucle infinie pour le maintien du fonctionnement du programme
            self.clock.tick(60) #Framerate fixé à 60 fps par seconde pour économiser le CPU.
            for event in pygame.event.get(): #Pour tous évènement pygame
                self.switch.checkEventBis(event)
                if event.type == pygame.QUIT: #Si on appuis sur la croix
                    self.switch.setEnd() #Aller sur le menu de fin
                #    self.dt.disconnect()
            if self.switch.getCurrentMenu() == Ordre_Menu.End: #Si le menu actuel est le menu de fin
                Q = True #La boucle infinie s’arrête

            pygame.display.update() #Rafraichit les élément à afficher

            self.surface.fill(self.fond) #Afficher le couleur de fond
            self.switch.checkEvent() #Lance la fonction checkEvent de la class Menu_switsh
            self.clientUpdater.updateClient(self.switch) #Update des variables du programme
            self.switch.affichage(self.surface) #Lance la fonction affichage de la class Menu_switsh
            self.switch.checkDataToSend(self.client) #Vérification des messages à envoyer
            self.client.sendData() #Envoi des messages

        pygame.quit()
