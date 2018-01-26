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

CESTA = 'http://10.50.8.20/data.xml'
APPNAME = 'pH Lavatec - '

class NalezenoExcept(Exception): pass

class Phlava(Frame):

    def ziskej(self):
        '''ziska data z prevodniku'''
        
        try:
            u = urlopen(CESTA,None,3)
            doc = parse(u)
            self.parent.title(APPNAME + 'ONLINE')
            
            try:            
                for ch in doc.findall('.//{http://www.papouch.com/xml/ad4eth/act}input'):
                    i = ch.attrib.get('id')
                    name = ch.attrib.get('name')
                    val = ch.attrib.get('val')
                    if(name == 'Ph Lavatec'):
                        raise NalezenoExcept()
                    
            except NalezenoExcept:
                self.ph = val
            
        except URLError as err:
            #nelze ziskat data
            print(err, file=sys.stderr)
            self.parent.title(APPNAME + 'OFFLINE')
            
        finally:
            self._update()
            self.after(5000, self.ziskej)
    
    def _update(self):
        #aktualizuje ph
        self.l.config(text='pH - '+str(self.ph))
        
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.ph = 7
        self.parent.resizable(False, False)
        self.l = ttk.Label(self.parent, text='pH', relief="ridge", font=(None, 100))
        self.l.pack(padx=10, pady=10)
        self.ziskej()
        
root = Tk()
app = Phlava(root)
app.mainloop()
