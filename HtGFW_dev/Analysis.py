import Zhihu
import os

def report():
    total_Posts = totalPosts()
    total_Censored = totalCensored()


def totalPosts():
    f = open('./topics.txt','r')
    amtFiles = 0
    for line in f:
        amtFiles += len([name for name in os.listdir('./'+line.strip())])
    f.close()
    return amtFiles

def totalCensored():
    files = [name for name in os.listdir('./Censored')]
    censored = 0
    for f in files:
        if not f == '.DS_Store':
            censored+=len([name for name in os.listdir('./Censored/'+f.strip())])
        
    return censored

def censoredByTopic():
    byTopic = {}
    topics = [name for name in os.listdir('./Censored')]
    for topic in topics:
        if not topic == '.DS_Store':
            byTopic[topic] = len([name for name in os.listdir('./Censored/'+topic.strip())])
    return byTopic

def printCensoredByTopic():
    byTopic = censoredByTopic()
    for k,v in byTopic.iteritems():
        print Zhihu.getTopicName(k)+' : '+str(v)
