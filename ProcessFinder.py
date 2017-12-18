import os, sys
import win32com.client
import pythoncom

class ProcessFinder:
    def __init__(self):
        self.getObj = win32com.client.GetObject('winmgmts:')

    def getProcessList(self):
        processList = []
        processes = self.getObj.InstancesOf('Win32_Process')
        for _ps in processes:
            processList.append(_ps.Properties_('Name').Value)
        return processList

    def findLolClient(self, processList):
        for _ps in processList:
            if _ps.find("League of Legends") != -1: # League of Legends
                print("find")
                return True
        return False

    def isLolStart(self):
        return self.findLolClient(self.getProcessList())

if __name__ == "__main__":

    a = ProcessFinder()

    import time
    while True:
        startTime = time.time()
        while time.time() - startTime < 7:
            None
        print(a.getProcessList())

