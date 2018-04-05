# -*- coding: utf-8 -*-
import Zhihu
import time
import os
import codecs


def main(topicFile = 'topics.txt'):
    dump = ''
    topics = open('./'+topicFile, 'r')
    for line in topics:
        line = line.strip()
        if not os.path.exists('./'+line.strip()):
            os.makedirs('./'+line.strip())
        dump += Zhihu.dumpTopic(line.strip())
    topics.close()
    dump_spl = dump.split('\n\n\n')
    #KEY (topicID+'\n'+posttype+'\n'+str(postid)+'\n'+question_url+'\n'+''+'\n'+title+'\n'+content+'\n\n')
    #KEY (topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author+'\n'+question_title+'\n'+ans_content+'\n\n')
    #KEY (topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author+'\n'+title+'\n'+art_content+'\n\n')

    for item in dump_spl:
        linespl = item.split('\n')
        if len(linespl) > 5:
            if not os.path.exists('./'+linespl[0]+'/'+linespl[2]):
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
    
                                      
            
            
            
    


main()
