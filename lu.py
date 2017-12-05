'''modul lu.py - laundry utils'''


#Trida Kus pro vypocet skladu, vlhkosti
class Kus:
    """Trida pro vypocet skladu, zbytkove vlhkosti"""
    
    #konstruktor
    def __init__(self, na):
        self.name = na
        #limitni velikost pro stohovac (cm)
        self.limit_sirka = 40
        self.limit_delka = 60
        #limitni velikost pro dvoudrahovy rezim vkladace Logic plus(cm)
        self.limit_2drahy = 150
        #rozmery
        self.sirka = 0
        self.delka = 0
        
    #vypocita pocet skladu
    def sklady(self,x,y):
        """Idelani pocet skladu"""
        if(x > self.limit_2drahy):
            dr = 1
        else:
            dr = 2
        if(x/4 > self.limit_sirka):
            x = x/8
            x -= 8 #odecte ohyb pradla
            xf = 3
        else:
            x = x/4
            x -= 5
            xf = 2
        if(y/4 > self.limit_delka):
            y = y/8
            yf = 3
        else:
            y = y/4
            yf = 2
        return[xf, yf, dr]
    
    #vkladani kratsi stranou
    def vkl_kratsi(self):
        self.l, self.x, self.dr = self.sklady(self.sirka, self.delka)
    
    #vkladani delsi stranou
    def vkl_delsi(self):
        """pouziti objekt.Vkl_delsi()"""
        self.l, self.x, self.dr = self.sklady(self.delka, self.sirka)
    
    #vypocet zbytkove vlkosti
    def vlhkost(pred, po):
        try:
            return round(((pred-po)/pred)*100, 2)
        except ZeroDivisionError:
            return 0
            
class Pipe:
    """Vypocita objem vody v trubce.
    Zadej __init__(prumer v mm)
    objem(delka v metrech)"""
    
    #kostruktor Pipe(prumer trubky v mm)    
    def __init__(self, prumer=50):
        self.prumer = prumer
            
    #vypocita objem vody v trubce dlouhe x metru    
    def objem(self, delka=1):
        from math import pi
        r = (self.prumer / 2) / 100
        h = delka * 10
        return int(pi * r**2 * h)

class Rph:
    """Vygeneruje nahodna mereni ph"""
    
    def __init__(self):
        
        self.data()
        
    def data(self):
        
        from random import random, randint
        self.ph_vrt = 7.2 + round(random(),2)
        self.ph_demi = 6.1 + round(random(),2)
        self.ph_upravena = 7.5 + round(random(),2)
        self.ph_lavatec = 6.2 + round(random(),2)
        self.ph_senking = 6.1 + round(random(),2)
        self.ec_demi = randint(30,53)
        self.ec_upravena = randint(1020,1080)
        self.ec_vrt = randint(1010,1040)
        self.ec_lavatec = randint(450,500)
        self.ec_senking = randint(380,450)
        
    def vypis(self):
        print("\n-------------------------------\n")
        print("Ph Demi - {0}".format(self.ph_demi))
        print("Vodivost demi - {0}ms\n".format(self.ec_demi))
        
        print("Ph Upravena - {0}".format(self.ph_upravena))
        print("Vodivost upravena - {0}ms\n".format(self.ec_upravena))
        
        print("Ph Vrt - {0}".format(self.ph_vrt))
        print("Vodivost vrt - {0}ms\n".format(self.ec_vrt))
        
        print("Ph Senking - {0}".format(self.ph_senking))
        print("Vodivost Senking - {0}ms\n".format(self.ec_senking))
        
        print("Ph Lavatec - {0}".format(self.ph_lavatec))
        print("Vodivost Lavatec - {0}ms".format(self.ec_lavatec))
        print("\n---------------------------------\n")
    
