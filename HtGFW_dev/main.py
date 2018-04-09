# -*- coding: utf-8 -*-
import Zhihu
import time
import os
import codecs
import smtplib
import datetime
import checker

def main(topicFile = 'topics.txt'):
    dump = ''
    topics = open('./'+topicFile, 'r')
    for line in topics:
        line = line.strip()
        if not os.path.exists('./'+line.strip()):
            os.makedirs('./'+line.strip())
        print '[+] DUMPING '+line.strip()+'...'
        dump += Zhihu.dumpTopic(line.strip())
    topics.close()
    dump_spl = dump.split('\n\n:\n')
    #KEY (topicID+'\n'+posttype+'\n'+str(postid)+'\n'+question_url+'\n'+''+'\n'+title+'\n'+content+'\n\n')
    #KEY (topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author+'\n'+question_title+'\n'+ans_content+'\n\n')
    #KEY (topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author+'\n'+title+'\n'+art_content+'\n\n')

    for item in dump_spl:
        linespl = item.split('\n')
        if len(linespl) > 6:
            if not os.path.exists('./'+linespl[0]+'/'+linespl[2]) and len(linespl[0]) == 8:
                topicid = linespl[0]
                posttype = linespl[1]
                postid = linespl[2]
                url = linespl[3]
                author = linespl[4]
                title = linespl[5]
                content = linespl[6]
                
                
                path = './'+topicid+'/'+postid
                textfile2 = codecs.open(path, 'a', encoding='utf-8')
                write = topicid+'\n'+posttype+'\n'+postid+'\n'+url+'\n'+author+'\n'+title+'\n\n'+content
                textfile2.write(write)
                textfile2.close()
    
                                      
            
            
            


email = raw_input('What EMail would you like to use? ')
passw = raw_input('What Password would you like to use? ')


counter = 4
while 1:
    try:
        
        main()
        amtFiles = 0
        f = open('./topics.txt','r')
        for line in f:
            
            amtFiles += len([name for name in os.listdir('./'+line.strip())])
        f.close()
        msg = 'There are currently '+str(amtFiles)+' files in search!'
        print datetime.datetime.now().strftime('%a, %d %B %Y %I: %M %S')+' : '+msg
        if (counter % 4) == 0:
            server = smtplib.SMTP('smtp.gmail.com',587, timeout=240)
            server.starttls()
            server.login(email.strip(), passw.strip())
            now = str(datetime.datetime.now().strftime('%a, %d %B %Y %I: %M %S'))
            report = open('./reports/'+datetime.datetime.now().strftime('%a, %d %B %Y %I: %M %S')+'.txt', 'w')
            time.sleep(60)
            report.write(checker.check())
            report.close()
            print now+'\n\n'+checker.stats()+'\n\n'+msg
            server.sendmail(email, email, msg)
            server.close()
            
            counter = 0
        time.sleep(600)
        counter +=1
        
    except Exception as e:
        server = smtplib.SMTP('smtp.gmail.com',587, timeout=120)
        server.starttls()
        server.login(email.strip(), passw.strip())
        now = str(datetime.datetime.now().strftime('%a, %d %B %Y %I: %M %S'))
        print now+' : ERROR: '+str(e)
        server.sendmail(email, email, now+' : ERROR: '+str(e))
        report = open('./reports/'+datetime.datetime.now().strftime('%a, %d %B %Y %I: %M %S')+'.txt', 'w')
        time.sleep(60)
        report.write(checker.check())
        server.close()
        
            
        time.sleep(120)
