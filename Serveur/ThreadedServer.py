import socket
from threading import Thread
from ServerUpdater import Updater
from DataHandler import DataHandler

import time

class ServerLoopers(Thread):

        def __init__(self):
                Thread.__init__(self) #initialisation du thread de la classe dans le constructeur
                
                self.clientsAdresses = [] #List contenant les adresses IP des clients
                self.clientsList = [] #Liste contenant les sockets correspondant à chaque client
                self.dataHandlerList = []

                self.serverPort = 60000 #Port d'écoute
                self.serverID = input("Merci d'entrer l'IP du serveur !") #IP du serveur à rentrer
                self.servAdr = self.serverID, self.serverPort #Variable nécéssaire pour bind la variable serveur à la ligne 24

                self.U = Updater() #La classe Updater se trouve Updater				


        def run(self): #méthode threadé
                self.server = socket.socket() #creation du socket serveur
                self.server.bind(self.servAdr) #Bind du socket sur l'ip et le port défini plus tôt
                self.server.listen(5) #On attent 5 connexionx maximum. Variera par la suite
                while True: #Boucle utilisé pour la connexion de nouveaux clients en parallèle du traitement des données reçu par les clients déjà connectés.
                        client, adr = self.server.accept() #Check si il y a une demande de connexion, si oui on l'accepte.
                        client.setblocking(0) #On passe le socket du client en mode non bloquand a fin de pouvoir en gérer plusieurs sans attente.
                        self.clientsList.append(client) #ajout du socket à la list de socket
                        self.clientsAdresses.append(adr) #ajout de l'adresse du client dans la liste d'adresses IP
                        D = DataHandler()
                        self.dataHandlerList.append(D)
                        print("connected ! : " + str(adr)) #Affiche "connected" une fois les opérations de connexion terminées.


                                
                                        

        def checkClients(self): #Méthode principale du serveur qui écoute les messages reçu des clients et gère les déconnexions.
                while True:
                        for i in range(len(self.clientsList)): #Parcour de la liste des clients
                                time.sleep(0.001) 
                                try: #Ici, on essaye d'envoyer un message au client, si il le reçoit on continue la fonction. Si une exception est levée on enlève le client de la liste et on retire son adresse IP (il ne reçoit pas les packet donc est potentiellement déconnecté.)
                                        msg = "$0000000000ct%"
                                        finalM = msg.encode('utf-8')
                                        self.clientsList[i].send(finalM)
                                except: #Gère l'enlèvement d'un client de la liste avec son adresse IP.
                                        print("Le client")
                                        print(self.clientsAdresses[i])
                                        print(" s'est déconnecté !")
                                        self.clientsList.remove(self.clientsList[i])
                                        self.clientsAdresses.remove(self.clientsAdresses[i])
                                        self.dataHandlerList.remove(self.dataHandlerList[i])
                                        break
                                try: #Si on reçoit un message du client alors on traite ce message via la classe DataHandler dont D est une instance sinon on passe car on a rien reçu.
                                                                             
                                        messageList = self.dataHandlerList[i].getIncomingDatas(self.clientsList[i])
                                        
                                        for j in range(len(messageList)):
                                                print('---------DEBUT RECU----------')
                                                print(messageList[j])
                                                a, b = self.dataHandlerList[i].splitPacketNameAndDatas(messageList[j])
                                                self.U.updateServerInfos(a, b)
                                                
                                                backMsg = self.U.getMessageToSendBack()
                                                print('---------FIN RECU----------')
                                                if len(backMsg) > 0: 
                                                        reponse = '$0000000000' + backMsg + '%'#Recuperation du messages à reenvoyer en fonction de la demande.
                                                        print(reponse)
                                                        final = reponse.encode('utf-8')
                                                        self.clientsList[i].send(final) #envoi
                                                
                                        
                                        
                                        #
                                except:
                                        pass

#On lance le thread et la boucle principale du serveur.

S = ServerLoopers()

S.start()
S.checkClients()

S.join()
