# -*- coding: utf-8 -*-
import Zhihu
import time
import os


def main(topicFile = 'topics.txt'):
    dump = ''
    topics = open('./'+topicFile, 'r')
    for line in topics:
        line = line.strip()
        if not os.path.exists('./'+line.strip()):
            os.makedirs('./'+line.strip())
        dump += Zhihu.dumpTopic(line.strip())
        dump_spl = dump.split('\n\n')
        
    for item in dump_spl:
        subs = item.split('\n')
        print item
        
##        if len(subs) > 5:
##            
##            postid = subs[2]
##            
##            url = subs[3]
##            author = subs[4]
##            #print '++++++++++++'+author+'++++++++++++'
##            type_post = subs[1]
##            topicid = subs[0]
##            path = './'+topicid+'/'+postid+''+author+'.txt'
##            
##            if not os.path.isfile(path):
##                
##                if type_post == 'article':
##                    newFile = open(path, 'w+')
##                    
##                    newFile.write(url+'\n')
##                    newFile.write(subs[6].encode('utf-8'))
##                    newFile.close()
##                else:
##                    #ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author+'\n'+ans_content+'\n'+question_title+'\n'+questionid+'\n'+question_url+'\n'+ques_content+'\n\n')
##                    ######subs[0]       subs[1]       subs[2]          subs[3] subs[4]      subs[5]          subs[6]             subs[7]         subs[8]           subs[9]
##                    print len(subs)
##                    
##                    newFile_ans = open(path, 'w+')
##                    
##                    newFile_ans.write(url+'\n')
##                    newFile_ans.write(subs[5].encode('utf-8'))
##                    newFile_ans.close()
##                    
##
##                    if not os.path.isfile('./'+topicid+'/'+subs[2]+subs[4]+'.txt'):
##                        #print('\n\n\n\n'+subs[6].encode('utf-8'))
##                        #print(subs[7].encode('utf-8'))
##                        
##                        newFile_ques = open('./'+topicid+'/'+subs[0]+subs[2]+'.txt', 'w+')
##                        
##                        newFile_ques.write(url+'\n')
##                        newFile_ques.write(subs[9].encode('utf-8'))
##                        newFile_ans.close()
    topics.close()
                                      
            
            
            
    


main()
