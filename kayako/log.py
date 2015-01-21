# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:25:01 2014

@author: nahum
"""
import io 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class log:
    
    def __init__(self):
        text = None
        self.filename = "log.txt"
    
    def create(self, text):
        stream = open(self.filename,"a")
        text = text + "\r\n"
        stream.write(text)
        
    def notification(self, subject,text):
        
        email_from="webmaster@nationalsoft.com.mx"
        email_to="isaikeb@gmail.com"
        
        message = MIMEMultipart("alternative")
        message["To"]= email_to
        message["From"] = email_from
        message["Subject"] = subject
                
        
        part = MIMEText(text,"plain")        
        message.attach(part)
        
        fp = open(self.filename, 'rb')
        content = MIMEText(fp.read(),"plain")
        fp.close()        
        message.attach(content)
        
        
        oSMTP = smtplib.SMTP("mail.nationalsoft.com.mx")
        oSMTP.login("test@nationalsoft.com.mx","33mlv3mS#")
        oSMTP.sendmail(email_from,email_to,message.as_string())
        oSMTP.quit()
        
        
