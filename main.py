from bs4 import BeautifulSoup
import requests


def get(url):
    headers = {'Accept':'','Accept-Encoding':'','Accept-Language':'','Cache-Control':'',
               'Connection':'','Cookie':'','Host':'','Upgrade-Insecure-Requests':'','User-Agent':''}
    cookies = 


def ping(url):
    res = requests.get(url).status_code
    print res
    return res == 200

def main(topicFile = 'topics.txt'):
    #TODO: check connectivity
    if not ping('https://www.zhihu.com'):
        print '[-] NETWORK CONNECTIVITY ISSUES'
        return 1
    #TODO: check topic availability
    #TODO: create filesystem
    #TODO: fetch posts
    
    

main()
