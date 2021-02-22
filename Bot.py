import random
import re
import os
import pyautogui as pag
import pydirectinput
import time
from colorama import init, Fore
import msvcrt

init(autoreset=True, convert=True)
pag.FAILSAFE = True
p = re.compile(r'\[(.*)\]')
o = re.compile(r'{(.*)}')
key = re.compile(r'KEY_([a-z0-9]+)')
tout = re.compile(r'TOUT_([0-9]+)')
tlr = re.compile(r'TLR_([.0-9]+)')
class Bot:
	def __init__(self, rootFolder = 'Images', startFolder = 'START'):
		self.rootFolder = './' + rootFolder + '/'
		self.currentFolder = startFolder

	def Run(self):
		while True:
			try:
				result = self.ProcessScreen(self.rootFolder + self.currentFolder, "0.98")
				if result:
					print('switch to {}{}'.format(Fore.GREEN, result))
					if result == 'END':
						print("Script stopped")
						break
					self.currentFolder = result
				k = kbfunc()
				if k == 113:
					exit()
				if k == 27:
					input("Press Enter to continue...")
					print("Script resumed")
			except KeyboardInterrupt:
				print('KeyboardInterrupt')
				break
		return

	def ProcessScreen(self, path, precisionDef):
		path = path if path[-1] == '/' or '\\' else path+'/'
		valid_images = [".jpg", ".gif", ".png", ".jpeg"]
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[1].lower() in valid_images]
		for file in files:
			opt = ExtractParam(o, file, None)
			precision = float(ExtractParam(tlr, opt, precisionDef))
			timeOut = int(ExtractParam(tout, opt, "0"))
			keyCode = ExtractParam(key, opt, None)
			pos = pag.locateCenterOnScreen(path+'/'+file, confidence = precision, grayscale=False)
			if pos:
				if keyCode:  
					pag.press(keyCode)  
					print('Presskey by {}{}'.format(Fore.RED, file))
				else:
					while pag.position().x != pos.x and pag.position().y != pos.y:
						pydirectinput.moveTo(pos.x, pos.y)
					pag.click()

					time.sleep(0.2)
					print('Click button {}{} {}{}'.format(Fore.RED, file, Fore.BLUE, pos))
				
				if timeOut > 0:    
					time.sleep(timeOut/1000)
				else:
					time.sleep(0.2)    

				return ExtractParam(p, file, None)
		return

def ExtractParam(r, text, defaultVal):
	if text:
		result = r.search(text)
		if result:
			return result.group(1)
	return defaultVal

def kbfunc():
	return ord(msvcrt.getch()) if msvcrt.kbhit() else 0
