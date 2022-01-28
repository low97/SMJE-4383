from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
	def _init_(self, parent=None):
		Frame._init_(self, parent)
		button = Button(self, text='press', command=self.reply)
		button.pack()
	def reply(self):
		showinfo(title='popup', message='Button pressed!')
		
if _name_ == "_main_":
	window = MyGui()
	window.pack()
	window.mainloop()