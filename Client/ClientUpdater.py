class ClientUpdater():
    """"""

    def __init__(self,dt,client): #initialisation des références à un client et à un DataHandler
        self.DH = dt
        self.client = client

    def updateClient(self,menuSwitch): #Récupération des données reçu et appel aux fonctions nécéssaires en fonction du message reçu
        l = self.DH.getIncomingDatas(self.client.getSocket())
        for n in range (len(l)) :
            name,data = self.DH.splitPacketNameAndDatas(l[n])
            
            if name == 'sendedQuestion' :
                self.updateQuestion(data, menuSwitch)
            if name == 'receivedScore':
                self.updateScore(data, menuSwitch)

    def updateQuestion(self,dataList,menuSwitch): #On change les texte des questions/réponses affichés
        print (dataList[0])
        menuSwitch.Menu2.t1.changeText(dataList[1])
        menuSwitch.Menu2.t2.changeText(dataList[2])
        menuSwitch.Menu2.t3.changeText(dataList[3])
        menuSwitch.Menu2.id = dataList[0]


    def updateScore(self,dataList,menuSwitch):
        menuSwitch.Menu2.popupScore.setStat(dataList[0],dataList[1]) #Actualisation du score affiché au joueur.
