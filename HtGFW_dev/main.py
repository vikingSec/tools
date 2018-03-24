
import Zhihu

def main(topicFile = 'topics.txt'):

    if not Zhihu.ping_url('https://www.zhihu.com'):
        print '[-] NETWORK CONNECTIVITY ISSUES'
        return 1
    print('[+] Connection Available')
    print(Zhihu.getPost('269692792',True))


main()
