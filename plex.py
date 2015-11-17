#python program that will scan an musicxml file, and at first, output the notes it finds :)

from tkinter import *
from tk.filedialog import askopenFileName

Tk().withdraw()
filestream = askopenFileName()
print(filestream)
