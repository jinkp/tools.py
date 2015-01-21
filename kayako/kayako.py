# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:50:10 2014

@author: N4hum
"""
import imaplib
import email
from datetime import date
from log import *

class kayako:
    
    def __init__(self):
        self.server= None        
        self.mailbox = None
        self.status = None
        self.host = None
        self.accounts = None
        self.notification = False
        self.currentAccount = None
        self.oLog = None
    
    def config(self,host):
        self.host = host;            
        
    def open(self,user,password):
        self.server = imaplib.IMAP4(self.host)
        self.server.login(user,password)
        
    def mailBox(self):
        server = self.server
        self.mailbox = None;
        server.select('inbox')
        status,mailbox = server.search('INBOX','ALL')
        self.mailbox = mailbox
        
        
    def check(self):
        server = self.server
        server.select('inbox')
        status,mailbox = server.search('INBOX','ALL')
        mail = None
        for num in mailbox[0].split():
            typ, data = server.fetch(num, '(FLAGS)')
            Seen = data[0].find("\Seen")            
            if Seen > 0:
                print ""                
        
    #Delete email from the server
    def delete(self):
        server = self.server        
        server.expunge()
        
    #Mark the email to delete
    def mark(self,msgid):
        server = self.server
        server.store(msgid, '+FLAGS', '\\Deleted')        
        
    #Close
    def close(self):
        server = self.server
        server.close()
        server.logout()
        
    #Delete emails with flags it's seen
    def scanMailRead(self):
        mailbox = self.mailbox                     
        for num in mailbox[0].split():
            typ, data = self.server.fetch(num, '(FLAGS)')
            Seen = data[0].find("\Seen")                           
            if Seen > 0:
                typ1, message = self.server.fetch( num, '(RFC822)')                
                if message[0]!= None:
                    raw_message = message[0][1]
                    message_email = email.message_from_string(raw_message)                    
                    lg = "\r\n ----BEGIN---- \r\n Eliminado   \r\n Asunto: " + message_email["Subject"] + " \r\n A:" + message_email["To"] +"   \r\n Desde:" + message_email["From"]+"\r\n -----END---- \r\n"
                else:
                    lg = "MSG ID: " + str(num) + " || No se encontró un mensaje"
                self.notification = True;
                self.mark(num)
                self.log(lg)        
        
        self.delete()
    
    def scan(self):
        for account in self.accounts:
            self.open(account[0],account[1])
            self.currentAccount = account[0]
            self.mailBox()            
            self.scanMailRead()
            self.close()
    
    #create a log
    def log(self,text):
        self.oLog = log()
        self.oLog.filename = "log" + str(date.today().day) + str(date.today().month) + str(date.today().year)+ ".txt"
        self.oLog.create(text)
        
    def logMail(self):
        if self.notification:
            self.oLog.notification("Kayako - Correo Eliminados de Cuentas ","Se han eliminado correos de las cuenta de Kayako.")
