from DatabaseHandler import DatabaseHandler

#classe qui gère les messages reçu et retourne un message à envoyer au client en fonction du message reçu.

class Updater():


	def __init__(self):
		print("Instance de PacketSelector")
		self.DBB = DatabaseHandler('DATABASE') #Création ou connexion à la base de donnée

		self.messageToSendBackToClient = ''

	def getMessageToSendBack(self): #on retourne le message à réenvoyer
		r = self.messageToSendBackToClient
		self.messageToSendBackToClient = ''
		return r

	#Fonction générale qui va appeler les fonctions nécéssaires en fonction du packet reçu et de son nom par exemple "Answer", "newQ" ou encore "Score".
	def updateServerInfos(self, packetName, datas):
		if packetName == "Answer":
			print('Réponse utilisateur reçu')
			self.receivedAnswer(datas)
		elif packetName == "newQ":
			print('Proposition de question reçu')
			self.receivedQuestion(datas)
		elif packetName == "Score":
			print('Demande de score reçu')
			self.receivedScoreAsking(datas)
		elif packetName == "QuestionAsk":
			print('Demande de question reçu !')
			self.receivedQuestionAsking()
		else :
			print("requete inconnue reçu !")


	#FONCTIONS UTILISANT LA BASE DE DONNEES -----------------------------------------------------------------------------------------------

	def receivedAnswer(self, answer): #Reçoit un message contenant la réponse d'un utilisateur
		questionID = int(answer[0])
		questionAnswer = int(answer[1])

		self.DBB.addScore(questionID, questionAnswer) #Actualisation de la base
		print('Vote ajouté à la réponse %s de la question numéro %s'% (questionAnswer, questionID))

		
	def receivedQuestion(self, questionAndAnswers): #Ajout d'une question à la base de donnée préalablement passé par un filtre anti insulte,... inclu dans le code client.
		QandR = [questionAndAnswers[0], questionAndAnswers[1], questionAndAnswers[2]]
		print(QandR)
		self.DBB.addQuestion(QandR[0], QandR[1], QandR[2], 2) #Actualisation de la base

	def receivedQuestionAsking(self): #Récupération d'une question au hasard
		ID = int(self.DBB.randomID(self.DBB.getIDs(1))) #On tire un ID au sort dans la base
		tab = self.DBB.searchQuestion(ID, 1) #Recuperation d'un ID de question au hasard dans la liste de la BDD puis on récup la quesiton
		self.messageToSendBackToClient = "sendedQuestion/%s/%s/%s/%s" % (ID, tab[0], tab[1], tab[2])
		print('Envoi de la question numéro : %s' %(ID))

	def receivedScoreAsking(self, questionIDstr): #Demande de score pour une question afin de l'afficher à l'utilisateur qui vient de répondre à une question d'ID : id
		
		ID = int(questionIDstr[0])
		scores = self.DBB.searchScore(ID)
		print('Scores de la question %s envoyés ! Les scores sont : %s.'%(ID, scores))
		self.messageToSendBackToClient = "receivedScore/%s/%s" % (scores[0], scores[1])
