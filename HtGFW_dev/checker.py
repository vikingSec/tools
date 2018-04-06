import Zhihu
import os
import datetime
import time

def stats():
    now = str(datetime.datetime.now().strftime('%a %d %B %Y %I: %M %S'))
    print now+'\n\n'

    amt_topics = len([name for name in os.listdir('./') if os.path.isdir('./'+name)])
    print 'NUMBER OF TOPICS: '+str(amt_topics)
    amt_posts = 0
    for sub in [name for name in os.listdir('./') if os.path.isdir('./'+name)]:
        amt_posts+=len([name for name in os.listdir('./')])
    print 'NUMBER OF POSTS: '+str(amt_posts)

def check():
    f = open('./topics.txt','r')
    for line in f:
        print 'CHECKING TOPIC: '+line.strip()
        path = './'+line.strip()+'/'
        for check in os.listdir(path):
            f = open(path+check.strip(),'r')
            spl = f.read().split('\n')
            Type = spl[1].strip()
            link = spl[3]

            CHECK = 'POTENTIALLY CENSORED: \n\n'
            
            if Type == 'article':
                res = Zhihu.get_url_zl(link)
                if not res.status_code == 200:
                    CHECK+= Type+' : '+str(res.status_code)+' : '+link+'\n'
            else:
                res = Zhihu.get_url(link)
                if not res.status_code == 200:
                    CHECK+= Type+' : '+str(res.status_code)+' : '+link+'\n'

    return CHECK
            
            
