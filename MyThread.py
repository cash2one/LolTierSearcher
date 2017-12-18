import threading
import time

import win32com.client
import pythoncom

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.apiGetter = None
        self.nickname = None
        self.popupMaker = None

    def setApiGetter(self, apiGetter):
        self.apiGetter = apiGetter

    def setNickname(self, nickname):
        self.nickname = nickname

    def setPopupMaker(self, popupMaker):
        self.popupMaker = popupMaker

    def run(self):
        id = self.apiGetter.getSummonerIdByName(self.nickname)
        while True:
            while not self.isLolStart():
                print("게임 대기중")
                time.sleep(15)

            print("게임 시작")
            time.sleep(5)

            gameInfo = self.apiGetter.getActiveGameInfo(id)
            while gameInfo == None:
                print("입장 대기중")
                time.sleep(5)
                gameInfo = self.apiGetter.getActiveGameInfo(id)


            enermy = self.apiGetter.getEnermySummonerTier(self.nickname, gameInfo)
            print(enermy)
            self.popupMaker.showTierInfo(enermy, 20000)

            while self.isLolStart():
                print("게임 종료 대기중")
                time.sleep(60)

    def isLolStart(self):
        pythoncom.CoInitialize()
        getObj = win32com.client.GetObject('winmgmts:')
        processList = []
        processes = getObj.InstancesOf('Win32_Process')
        for _ps in processes:
            processList.append(_ps.Properties_('Name').Value)

        for _ps in processList:
            if _ps.find("League of Legends") != -1:  # League of Legends
                print("find")
                return True
        return False
