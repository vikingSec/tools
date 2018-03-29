import Zhihu
import time
import os

def main(topicFile = 'topics.txt'):

    topics = open('./'+topicFile, 'r')
    for line in topics:
        line = line.strip()
        if not os.path.exists('./'+line.strip()):
            os.makedirs('./'+line.strip())
        dump = Zhihu.dumpTopic(line.strip())
        dump_spl = dump.split('\n\n')
        
        for item in dump_spl:
            subs = item.split('\n')
            
            if len(subs) > 2:
                postid = subs[2]
                url = subs[3]
                author = subs[4]
                type_post = subs[1]
                path = './'+line+'/'+postid+author+'.txt'
                if not os.path.isfile(path):
                    
                    if type_post == 'article':
                        newFile = open(path, 'w+')
                        newFile.write(url+'\n'+subs[6])
                        newFile.close()
                    else:
                        newFile_ans = open(path, 'w+')
                        newFile_ans.write(url+'\n'+subs[5])
                        newFile_ans.close()

                        if not os.path.isfile('./'+line+'/'+subs[8]+'.txt'):
                            newFile_ques = open('./'+line+'/'+subs[7]+subs[6]+'.txt', 'w+')
                            newFile_ques.write(url+'\n'+subs[9])
                            newFile_ans.close()
    topics.close()
                                      
            
            
            
    


main()
