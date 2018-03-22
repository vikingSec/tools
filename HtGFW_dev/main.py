import Zhihu

def main(topicFile = 'topics.txt'):
   
    if not Zhihu.ping_url('https://www.zhihu.com'):
        print '[-] NETWORK CONNECTIVITY ISSUES'
        return 1
    print('[+] Connection Available')
    

main()
