import pythoncom
import win32com.client

pythoncom.CoInitialize()
getObj = win32com.client.GetObject('winmgmts:')
processList = []
processes = getObj.InstancesOf('Win32_Process')
for _ps in processes:
	processList.append(_ps.Properties_('Name').Value)

print(processList)