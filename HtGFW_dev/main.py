import Zhihu
import time

def main(topicFile = 'topics.txt'):

    f = open('./topics.txt', 'r')
    content = f.readlines()
    for line in content:
        print Zhihu.dumpTopic(line.strip())
    f.close()


main()
