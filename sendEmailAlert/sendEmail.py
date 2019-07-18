# -*- coding: utf-8 -*-
import time
import smtplib
import threading



def sendEmailAlertFunc():
    gmail_user = 'bot.zealvirtualcompany@gmail.com'  
    gmail_password = 'ZealVCBot2018'
    sent_from = gmail_user  
    to = ['phokchanrithisak@gmail.com',
          'phokchanrithisak16@kit.edu.kh',
          'zeal@kit.edu.kh',
          'sanysaklucky@gmail.com'
          ]  
    subject = 'DETECTION ALERT - ZEAL BOT (noreply)'  
    body = "Streaming IP Camera Oculus Go, Wild animals detection alert, Please contact Rithisak XXXXXXX" 
    email_text = """
    From: %s  
    To: %s  
    Subject: %s
      
    %s
    """ % (sent_from, ", ".join(to), subject, body)
                 
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print ('====Email Sent Successfully====')
    except:  
        print ('You Are Offline!')
        
    
    #time.sleep(1)  
    #threading.Timer(5, sendEmailAlert).start()
    #print('KIT Detected:', time.ctime())
    #threading.Timer(30, sendEmailAlertFunc).start()
