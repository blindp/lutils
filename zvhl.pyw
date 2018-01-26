#!/usr/bin/python3
"""

Vypocita zbytkovou vlhkost pradla
Blind Pew 2017 <blind.pew96@gmail.com>
GNU GPL v3

"""

from tkinter import Tk, Label, LabelFrame, Button, Entry, IntVar, W, E
import lu

class Vlhkost:
    
    def __init__(self, parent):
        self.parent = parent
        parent.title("Zbytková vlhkost")
        parent.resizable(False, False)
        self.wet = IntVar()
        self.dry = IntVar()
        self.per = 0
        
        self.label_in = LabelFrame(parent, text="Váha před")
        self.label_out = LabelFrame(parent, text="Váha po")
        self.labelf_per = LabelFrame(parent, text="Zbytková vlhkost")
        self.entry_in = Entry(self.label_in, textvariable=self.wet)
        self.entry_out = Entry(self.label_out, textvariable=self.dry)
        self.butto = Button(self.labelf_per, text="Vypočítej", command=lambda: self.pocitej())
        self.label_per = Label(self.labelf_per, text="0")
        self.pocitej()
        
        #rozvrzeni
        self.label_in.grid(row=0, column=0, sticky=W+E, padx=10, pady=5)
        self.entry_in.grid(row=0, column=0, sticky=W+E, padx=5, pady=5)
        self.label_out.grid(row=1, column=0, sticky=W+E, padx=10, pady=5)
        self.entry_out.grid(row=0, column=0, sticky=W+E, padx=5, pady=5)
        self.labelf_per.grid(row=2, column=0, sticky=W+E, padx=10, pady=5)
        self.butto.grid(row=0, column=0, sticky=W+E, padx=5, pady=5)        
        self.label_per.grid(row=0, column=1, sticky=W+E, padx=5, pady=5)
        
    def pocitej(self):
        a = self.wet.get()
        b = self.dry.get()
        self.per = lu.Kus.vlhkost(a,b)
        self.label_per.config(text=str(self.per)+" %")
        
root = Tk()
hlavni = Vlhkost(root)
root.mainloop()
