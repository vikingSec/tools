import Zhihu
import os
import datetime
import time
import shutil

def stats():
    ret = ""
    now = str(datetime.datetime.now().strftime('%a %d %B %Y %I: %M %S'))
    ret+=now+'\n\n'
    
    amt_topics = len([name for name in os.listdir('./') if os.path.isdir('./'+name)])
    ret+='NUMBER OF TOPICS: '+str(amt_topics)+'\n'

    return ret

def check():
    f = open('./topics_1.txt','r')
    CHECK = 'POTENTIALLY CENSORED: \n\n'
    for line in f:
        print 'CHECKING TOPIC: '+line.strip()
        path = './'+line.strip()+'/'
        for check in os.listdir(path):

            time.sleep(8)
            f = open(path+check.strip(),'r')
            spl = f.read().split('\n')
	    if len(spl) > 1:
            	    Type = spl[1].strip()
            	    link = spl[3]

            
            
                    if Type == 'article':
                        res = Zhihu.get_url_zl(link)
                	if not res.status_code == 200:
                    	    print Type+' : '+str(res.status_code)+' : '+link+'\n'
                    	    CHECK+= Type+' : '+str(res.status_code)+' : '+link+'\n'
                    	    if not os.path.exists('./Censored/'+path.strip().replace('./','')):
                                os.makedirs('./Censored/'+path.strip().replace('./',''))
                    	    shutil.copy2(path+check.strip(), './Censored/'+path.strip().replace('./',''))
                    else:
                        res = Zhihu.get_url(link)
                        if not res.status_code == 200:
                            print Type+' : '+str(res.status_code)+' : '+link+'\n'
                            CHECK+= Type+' : '+str(res.status_code)+' : '+link+'\n'
                            if not os.path.exists('./Censored/'+path.strip().replace('./','')):
                                os.makedirs('./Censored/'+path.strip().replace('./',''))
                            shutil.copy2(path+check.strip(), './Censored/'+path.strip().replace('./',''))
    return CHECK
            
            
