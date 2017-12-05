#!/usr/bin/python3
"""

Zobrazeni hodnoty ph linky Lavatec z prevodniku AD4ETH <papouch.com>
Blind Pew 2017 <blind.pew96@gmail.com>
GNU GPL v3

"""
import sys
from urllib.request import urlopen
from urllib.error import URLError
from xml.etree.ElementTree import parse
from tkinter import Tk, Frame, ttk

CESTA = 'http://192.168.1.254/data.xml'
APPNAME = 'Ph Lavatec - '

class NalezenoExcept(Exception): pass

class App(Frame):

    def ziskej(self):
        '''ziska data z prevodniku'''
        
        try:
            u = urlopen(CESTA,None,3)
            doc = parse(u)
            self.parent.title(APPNAME + 'ONLINE')
            
        except URLError as err:
            #nelze ziskat data pouzij mistni soubor
            print(err, file=sys.stderr)
            self.parent.title(APPNAME + 'OFFLINE')
            try:
                doc = parse('data.xml')
            except FileNotFoundError:
                print("Nemohu pokracovat :-(", file=sys.stderr)
                sys.exit(0)
            
        try:            
            for ch in doc.findall('.//{http://www.papouch.com/xml/ad4eth/act}input'):
                i = ch.attrib.get('id')
                name = ch.attrib.get('name')
                val = ch.attrib.get('val')
                if(name == 'Lavatec'):
                    raise NalezenoExcept()
                    
        except NalezenoExcept:
            self.l.config(text='Ph - '+str(val))
        
        finally:
            self.after(5000, self.ziskej)
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(False, False)
        self.l = ttk.Label(self.parent, text='Ph', relief="ridge", font=(None, 100))
        self.l.pack(padx=10, pady=10)
        self.ziskej()
        
root = Tk()
app = App(root)
app.mainloop()
