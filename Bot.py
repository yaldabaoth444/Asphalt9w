import random
import re
import os
import pyautogui as pag
import pydirectinput
import time

pag.FAILSAFE = True
p = re.compile(r'\[(?P<path>.*)\]')
o = re.compile(r'{(?P<options>.*)}')
key = re.compile(r'KEY_([a-z0-9]+)')
tout = re.compile(r'TOUT_([0-9]+)')
tlr = re.compile(r'TLR_([.0-9]+)')

class Bot:
	def __init__(self):
		pass

	def Run(self, startPath):
		root = './Images/'
		path = startPath
		while True:
			try:
				result = self.ProcessScreen(root + path, 0.98)
				if result:
					print('switch to ' + result)
					path = result

			except KeyboardInterrupt:
				print('KeyboardInterrupt')
				break
		return
	
	def ProcessScreen(self, path, precisionDef):
		path = path if path[-1] == '/' or '\\' else path+'/'
		valid_images = [".jpg", ".gif", ".png", ".jpeg"]
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[1].lower() in valid_images]
		for file in files:
			precision = precisionDef
			m_opt = o.search(file)
			timeOut = 0
			keyCode = None
			opt = None 
			if m_opt:
				opt = m_opt.group('options')

				m_tlr = tlr.search(opt)
				if m_tlr:
					precision = float(m_tlr.group(1))
					#print('custom precision = {}'.format(precision))
				
				m_opt = key.search(opt)
				if m_opt:
					keyCode = m_opt.group(1)
					#print('key = {}'.format(keyCode))

				m_tout = tout.search(opt)
				if m_tout:
					timeOut = int(m_tout.group(1))
					#print('timeout  = {}'.format(timeOut))

			pos = pag.locateCenterOnScreen(path+'/'+file, confidence = precision, grayscale=False)
			if pos:
				print(pos)
				if keyCode:  
					pag.press(keyCode)  
					print('Presskey {} by {}'.format(keyCode, file))
				else:
					while pag.position().x != pos.x and pag.position().y != pos.y:
						pydirectinput.moveTo(pos.x, pos.y)
					pag.click()

					time.sleep(0.2)
					print('Click to button {}'.format(file))
				
				if timeOut > 0:    
					time.sleep(timeOut/1000)
				else:
					time.sleep(0.2)    

				m_path = p.search(file)
				if m_path:
					return m_path.group('path')
		return