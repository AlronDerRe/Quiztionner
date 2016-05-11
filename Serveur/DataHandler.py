import socket

class DataHandler():

	def __init__(self):
		self.receivedMessage = []
		self.currentMessage = ""
		self.currentMessageToComplete = -1
		self.decodedMessages = []

	def getIncomingDatas(self,socket): #Thread qui affiche les messages reçu si pas de message, on recommence : "pass" ligne 22.
			try:
				self.decodedMessages = []
				mess = socket.recv(1024)
				readableMSG = mess.decode('utf-8')

				for i in range(len(readableMSG)):
					if readableMSG[i] == '%':
						self.receivedMessage.append(self.currentMessage)
					elif readableMSG[i] == '$':
						self.currentMessage = ""
					else:
						self.currentMessage += readableMSG[i]



				for a in range(len(self.receivedMessage)):
					if self.receivedMessage[a][:10] == '0000000000':
						if self.receivedMessage[a][10:] != 'ct' :
							self.decodedMessages.append(self.receivedMessage[a][10:])

				self.receivedMessage = []

				return self.decodedMessages

			except:
				return self.decodedMessages

	def splitPacketNameAndDatas(self, message):
		char = ''
		packetName = ""
		datas = ""
		counter = -1
		while char != '/':
			packetName += char
			counter+=1
			char = message[counter]
		counter += 1
		while counter < len(message):
			char = message[counter]
			datas += char
			counter+=1
		
		
		dataList = ['']
		counterBis = 0
		for i in range(len(datas)):
			if datas[i] == '/':
				dataList.append('')
				counterBis=counterBis+1
			else:
				dataList[counterBis] = dataList[counterBis] + datas[i]
		
		return (packetName, dataList)
