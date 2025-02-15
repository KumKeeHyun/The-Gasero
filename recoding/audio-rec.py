from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import pyaudio
import wave
import os


class Rec:
	def __init(self, chunk = 1024, frmt = pyaudio.paInt16, channels = 1, rate = 44100, py = pyaudio.PyAudio()):
	
		self.main = tkinter.Tk()
		self.collections = []
		self.main.geometry('500x300')
		self.main.title('Record')
		self.CHUNK = chunk
		self.FORMAT = frmt
		self.CHANNELS = channels
		self.RATE = rate
		self.p = py
		self.frames = []
		self.st = 1
		self.stream = self.p.open(format = self.FORMAT, 
								channels = self.CHANNELS,
								rate = self.RATE,
								input = True,
								frames_per_buffer = self.CHUNK)

		self.buttons = tkinter.Frame(self.main, padx=120, pady=20)

		self.buttons.pack(fill = tk.BOTH)

		label1 = ttk.Label(root, text = 'File Name')
		label1.grid(row = 0, column = 0)

		entry1 = ttk.Entry(root, width = 40) 
		entry1.grid(row = 0, column = 2, columnspan = 4)

		label2 = ttk.Label(root, text = 'Your Text')
		label2.grid(row = 4, column = 0)

		entry2 = ttk.Entry(root, width = 40)
		entry2.grid(row = 4, column = 2, columnspan = 4)
	
		MyButton1 = ttk.Button(root, text='Start', width=10, padx=10, pady=5, command=lambda: self.start_rec())
		MyButton1.grid(row = 0, column = 8, padx=50, pady=5)

		MyButton2 = ttk.Button(root, text='Stop', width=10, padx=10, pady=5, command=lambda: self.stop_rec())
		MyButton2.grid(row = 0, column = 18, padx=50, pady=5)

		tkinter.mainloop()

		def start_rec(self):
			self.st = 1
			self.frames = []
			self.stream = self.p.open(format = self.FORMAT, 
								channels = self.CHANNELS,
								rate = self.RATE,
								input = True,
								frames_per_buffer = self.CHUNK)

			while self.st == 1 :
				data = stream.read(self.CHUNK)
				self.frames.append(data)
				self.main.update()

			stream.close()

		
root = tk.Tk()
root.title('Recorder')

label1 = ttk.Label(root, text = 'File Name')
label1.grid(row = 0, column = 0)

entry1 = ttk.Entry(root, width = 40) 
entry1.grid(row = 0, column = 2, columnspan = 4)

label2 = ttk.Label(root, text = 'Your Text')
label2.grid(row = 4, column = 0)

entry2 = ttk.Entry(root, width = 40)
entry2.grid(row = 4, column = 2, columnspan = 4)

##definitions here
def callback():
	if len(entry1.get()) == 0:
		messagebox.showinfo("Error", "Enter File Name")
	else:
		word = entry1.get()
		record.record_audio(word)

def stop():
	#work in progress

def quit():
	sys.exit()

def save_text():
	#work in progress

###


MyButton1 = ttk.Button(root, text='Start', width=10, command=callback)
MyButton1.grid(row = 0, column = 8)

MyButton2 = ttk.Button(root, text='Stop', width=10, command=stop)
MyButton2.grid(row = 0, column = 18)

MyButton3 = ttk.Button(root, text = 'Save Text', width=10, command=save_text)
MyButton3.grid(row = 4,column = 8)

MyButton4 = ttk.Button(root, text = 'Quit', width=10, command=quit)
MyButton4.grid(row = 4, column = 18)

root.mainloop()
