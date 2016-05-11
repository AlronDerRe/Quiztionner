class ClientUpdater():
    """"""

    def __init__(self,dt,client):
        self.DH = dt
        self.client = client

    def updateClient(self,menuSwitch):
        l = self.DH.getIncomingDatas(self.client.getSocket())
        for n in range (len(l)) :
            name,data = self.DH.splitPacketNameAndDatas(l[n])
            
            if name == 'sendedQuestion' :
                self.updateQuestion(data, menuSwitch)
            if name == 'receivedScore':
                self.updateScore(data, menuSwitch)
                print('sdggggg------')

    def updateQuestion(self,dataList,menuSwitch):
        print (dataList[0])
        menuSwitch.Menu2.t1.changeText(dataList[1])
        menuSwitch.Menu2.t2.changeText(dataList[2])
        menuSwitch.Menu2.t3.changeText(dataList[3])
        menuSwitch.Menu2.id = dataList[0]


    def updateScore(self,dataList,menuSwitch):
        menuSwitch.Menu2.popupScore.setStat(dataList[0],dataList[1])
