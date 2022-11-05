import pyautogui
import platform
import time
import os
from subprocess import call

system  = platform.system()
msg1 = ["A","r","e"," ","y","o","u"," ","s","c","a","r","e","d","?"]

pyautogui.alert(text="Tüm bilgisayarı çökertmeye çalışan kötü amaçlı yazılım tespit edildi. Program kapatılıp siliniyor...",title=system +" "+ "Güvenlik Duvarı",button="Tamam")
time.sleep(10)
pyautogui.alert(text="Fatal: D€@₺h adlı virüs dosyası silinemiyor.",title=system + " " + "Hata Ayıklama Konsolu",button="Tamam")

if system == "Windows":
	pyautogui.hotkey('win','r')
	pyautogui.typewrite("cmd")
	pyautogui.press('enter')
	pyautogui.typewrite("mkdir hacked")
	pyautogui.press('enter')
	pyautogui.typewrite("cd hacked")
	pyautogui.press('enter')
	pyautogui.typewrite("nano msg.txt")
	pyautogui.press('enter')
	time.sleep(1)
	for i in msg1:
		pyautogui.press(i)
		tiem.sleep(0.5)
	pyautogui.alert(text="C:\\Users adlı dosya siliniyor...",title=system + " "+"Denetim Masası",button="Tamam")
	time.sleep(3)
	pyautogui.alert(text="C:\\Windows adlı dosya siliniyor...",title=system+" "+"Denetim Masası", button="Tamam")
	cwd=os.getcwd()
	bsod=os.path.join(cwd,"bsod.py")
	class CallPy(object):
		def __init__(self,path=bsod):
			self.path=path
		def call_python_file(self):
			call(["Python3","{}".format(self.path)])

	if __name__ == "__main__":
		c=CallPy()
		c.call_python_file()

