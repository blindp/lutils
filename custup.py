#!/usr/bin/python3
"""
Upload 'custart.csv' to jensen machine.
Blind Pew 2017 <blind.pew96@gmail.com>
GNU GPL v3
"""

import sys
import machine


l = 'D'
linka = []

for i in range(len(machine.Const.SERIAL[l])):
    linka.append(machine.Machine(machine.Const.NAME[i],
                                    machine.Const.IP[i],
                                    machine.Const.SERIAL[l][i]))

def pouziti():
    print("\nUsage:",sys.argv[0],"<filename>\n")

if(len(sys.argv)>1):
    soubor = sys.argv[1]
else:
    pouziti()
    sys.exit(0)

for stroj in linka:
    
    try:
        stroj.connect()
        stroj.custup(soubor)
        stroj.disc()
    except Exception as err:
        print(
                machine.Const.ANSI_COLOR['red']+
                "Error on upload - {0}".format(stroj.name)+
                machine.Const.ANSI_COLOR['end'])
        print(err)
