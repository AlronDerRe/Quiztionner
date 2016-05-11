from DatabaseHandler import DatabaseHandler

#classe qui gère les messages reçu et retourne un message à envoyer au client en fonction du message reçu.

class Updater():


	def __init__(self):
		print("Instance de PacketSelector")
		self.DBB = DatabaseHandler('DATABASE')

		l = self.DBB.getIDs(1)
		print(l)
		self.messageToSendBackToClient = ''

	def getMessageToSendBack(self):
		r = self.messageToSendBackToClient
		self.messageToSendBackToClient = ''
		return r

	#Fonction générale qui va appeler les fonctions nécéssaires en fonction du packet reçu et de son nom par exemple "Answer", "newQ" ou encore "Score".
	def updateServerInfos(self, packetName, datas):
		if packetName == "Answer":
			print('receivedAnswer')
			self.receivedAnswer(datas)
		elif packetName == "newQ":
			print('receivedQuestion')
			self.receivedQuestion(datas)
		elif packetName == "Score":
			print('receivedScoreAsking')
			self.receivedScoreAsking(datas)
		elif packetName == "QuestionAsk":
			print('Demande de question reçu !')
			self.receivedQuestionAsking()
		else :
			print("requete inconnue reçu !")


	#FONCTIONS UTILISANT LA BASE DE DONNEES -----------------------------------------------------------------------------------------------

	def receivedAnswer(self, answer): #Reçoit un message demandant de renvoyer une question à laquelle répondre au client.
		questionID = int(answer[0])
		questionAnswer = int(answer[1])

		print(questionID)
		print(questionAnswer)

		self.DBB.addScore(questionID, questionAnswer)
		print('ok3')

		#self.messageToSendBackToClient = "La réponse a bien été enregistrée !" #ICI on renverra un message contenant les informations de score relatif à cette question

	def receivedQuestion(self, questionAndAnswers): #Ajout d'une question à la base de donnée préalablement passé par un filtre anti insulte,... inclu dans le code client.
		QandR = [questionAndAnswers[0], questionAndAnswers[1], questionAndAnswers[2]]
		
		self.messageToSendBackToClient = "La question a bien été reçue !/1" #Message de retour
		print(QandR)
		self.DBB.addQuestion(QandR[0], QandR[1], QandR[2], 1)

	def receivedQuestionAsking(self):
		print('dacc')
		ID = int(self.DBB.randomID(self.DBB.getIDs(1)))
		print(ID)
		tab = self.DBB.searchQuestion(ID, 1) #Recuperation d'un ID de question au hasard dans la liste de la BDD puis on récup la quesiton
		print('dacc2')
		self.messageToSendBackToClient = "sendedQuestion/%s/%s/%s/%s" % (ID, tab[0], tab[1], tab[2])
		print(self.messageToSendBackToClient)


	def receivedScoreAsking(self, questionIDstr): #Demande de score pour une question afin de l'afficher à l'utilisateur qui vient de répondre à une question d'ID : id
		
		ID = int(questionIDstr[0])
		scores = self.DBB.searchScore(ID)
		print(scores)
		self.messageToSendBackToClient = "receivedScore/%s/%s" % (scores[0], scores[1])
