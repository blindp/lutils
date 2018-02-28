"""Modul for jensen laundry machine"""

import os, sys, datetime
from ftplib import FTP
from config import *
    
class Utils:
    """help utils"""
    
    def chlp(path):
        """check local path"""
        path = path.lower()
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                os.chdir(path)
            except:
                print("I can not create: {0}".format(path))
                sys.exit(0)
        else:
            try:
                os.chdir(path)
            except:
                pass
    
    def lastm():
        """return last month of year file mask log file"""
        x = '*-'
        d = datetime.datetime.now()
        if(d.month > 1):
            rok = d.year
            x = x + str(d.month-1)
            x = x + '-'
        else:
            x = x + str(12)
            rok = d.year-1
            x = x + '-'
        x = x + str(rok) + '_log.csv'
        return x
        
class Machine:
    """main class"""
    
    def __init__(self, name, ip, serial=False):
        self.name = name
        self.ip = ip
        self.serial = serial
        self.a_rcf = ''
        
    def connect(self):
        """connect to B&R PLC"""
        self.ftp = FTP(self.ip, timeout=3)
        self.ftp.login(Const.LOGIN,Const.PASSW)
        
    def disc(self):
        """quit ftp"""
        self.ftp.quit()
    
    def custup(self,filename):
        """upload 'custart.csv'"""
        self.ftp.cwd(Const.PATH_CUST)
        name = os.path.basename(filename)
        try:
            self.ftp.storbinary("STOR " + name, open(filename, 'rb'))
        except:
            print("I can not upload: {0}".format(filename))
    
    def backup(self):
        """backup directory jensen"""
        local_path = Const.PATH_LOCAL+self.serial+'/'
        self.ftp.cwd(Const.PATH_JEN)
        seznam = self.ftp.nlst()
        seznam = seznam[2:]
        for x in seznam:
            print(Const.ANSI_COLOR['magenta'] + "Path - {0}".format(local_path+x)+Const.ANSI_COLOR['end'])
            Utils.chlp(local_path+x)
            self.ftp.cwd(Const.PATH_JEN+'/'+x)
            for filename in self.ftp.nlst(Const.MASK):
                try:
                    print(filename)
                    fh = open(filename.lower(), 'wb')
                    self.ftp.retrbinary('RETR ' + filename, fh.write)
                    fh.close()
                except:
                    print("I can not download: {0}".format(filename))
                        
    def save_statis(self):
        """save statistic of last month"""
        local_path = Const.PATH_LOCAL+Const.DIR_STAT+self.serial
        self.ftp.cwd(Const.PATH_STAT)
        Utils.chlp(local_path)
        print(Const.ANSI_COLOR['yellow']+"Downloading statistics..."+Const.ANSI_COLOR['end'])
        for filename in self.ftp.nlst(Utils.lastm()):
            try:
                print(filename)
                fh = open(filename.lower(), 'wb')
                self.ftp.retrbinary('RETR ' + filename, fh.write)
                fh.close()
            except:
                print("I can not download: {0}".format(filename))
                
    def del_statis(self):
        """delete all statistic !!!!"""
        self.ftp.cwd(Const.PATH_STAT)
        for filename in self.ftp.nlst(Const.MASK):
            self.ftp.delete(filename)
    
    def info(self):
        """machine info"""
        print(Const.ANSI_COLOR['yellow']+"Sn: {2} at {1} - {0}".format(self.name,self.ip,self.serial)+Const.ANSI_COLOR['end'])
        
    def _last_rcp(self):
        """get last loaded recipe file"""
        import csv
        with open(Const.PATH_LOCAL+self.serial+'/system/system.csv') as sys_csv:
            reader = csv.DictReader(sys_csv, delimiter=';')
            for row in reader:
                if(row[''] == 'SystemFileData.LastLoadedRecipe'):
                    #print("Nalezeno: {1} - {0}".format(row['1'], self.name))
                    self.a_rcf = row['1']
