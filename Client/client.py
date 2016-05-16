import socket


class Client():

	adrServ = input("Merci d'entrer l'IP du serveur !"), 60000 #On rentre l'ip et on attend au port 60000

	def __init__(self): #Connection du client au serveur grâce à adrServ, le socket passe ensuite en mode non bloquant(ligne 12). Initialisation du thread d'écoute de messages reçu
		self.client = socket.socket()
		self.client.connect(self.adrServ)
		self.client.setblocking(0)

		self.dataList = [] #creation de la liste de messages à envoyer à chaque tour de boucle


	def addDataToSend (self, data): #ajout d'un message à envoyer 
		self.dataList.append(data)

	def sendData (self): #Envoi des données si il y en a
		while len(self.dataList) > 0 :
			v = self.dataList[0].encode('utf-8')
			self.client.send(v)
			print (self.dataList[0])
			self.dataList.remove(self.dataList[0])

	def disconnect (self): #déconnexion
		self.client.close()
#Instanciation du DataReceiver du client

	def getSocket(self): #récupération du socket depuis l'extérieur de la classe
		return self.client
