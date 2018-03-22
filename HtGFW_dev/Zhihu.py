from bs4 import BeautifulSoup
import requests

def get_url(url):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5',
               'Cache-Control':'max-age=0','Connection':'keep-alive',
               'Cookie':'q_c1=a425ea5549a447938faa642092051460|1521440815000|1516935035000; _zap=40223734-45c7-4aa7-b889-455b19f112f8; _xsrf=fe01d4d6-3efc-4ce4-8cce-c23c926e083d; d_c0="ALCrrMlPTw2PTtdc-_V6691f11FzKrIW34I=|1521440815"; capsion_ticket="2|1:0|10:1521441001|14:capsion_ticket|44:ODY0ODIwNDY3MTZjNDQ2ZWEzMzY0MTUyYmUzYmIyY2Y=|8999178ca9eca48ff5a58634ff875758f0c652faf570b4cdfff44b58b7ee1451"; z_c0="2|1:0|10:1521441122|4:z_c0|92:Mi4xMGxGbEF3QUFBQUFBc0t1c3lVOVBEU1lBQUFCZ0FsVk5ZcWVjV3dEclpxYVVzcW5oN2RsUmJfejJuaVFfTGViN0hR|146622b2b39772b7212ae40b7b59217bcccca30163f184628ef96ed9744cf452"; unlock_ticket="AADALBf8cQomAAAAYAJVTWpgr1qJugy4PDM7_uLRXnNshPuWB12czg=="',
               'Host':'www.zhihu.com','Upgrade-Insecure-Requests':'1',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 GoogleChrome'}
    '''cookies = {'_xsrf':'fe01d4d6-3efc-4ce4-8cce-c23c926e083d',
               '_zap':'40223734-45c7-4aa7-b889-455b19f112f8',
               'capsion_ticket':'"2|1:0|10:1521441001|14:capsion_ticket|44:ODY0ODIwNDY3MTZjNDQ2ZWEzMzY0MTUyYmUzYmIyY2Y=|8999178ca9eca48ff5a58634ff875758f0c652faf570b4cdfff44b58b7ee1451"',
               'd_c0':'"ALCrrMlPTw2PTtdc-_V6691f11FzKrIW34I=|1521440815"',
               'q_c1':'a425ea5549a447938faa642092051460|1521440815000|1516935035000',
               'unlock_ticket':'"AADALBf8cQomAAAAYAJVTWpgr1qJugy4PDM7_uLRXnEshPuWB12czg=="',
               'z_c0':'"2|1:0|10:1521441122|4:z_c0|92:Mi4xMGxGbEF3QUFBQUFBc0t1c3lVOVBEU1lBQUFCZ0FsVk5ZcWVjV3dEclpxYVVzcW5oN2RsUmJfejJuaVFfTGViN0hR|146622b2b39772b7212ae40b7b59217bcccca30163f184628ef96ed9744cf452"'} 
    '''
    return requests.get(url, headers=headers)

def ping_url(url):
    res = get_url(url)
    return res.status_code == 200

def ping_topic(topic):
    res = get_url('https://www.zhihu.com/topic/'+topic.strip()+'/hot')
    return res.status_code == 200

def getTopicName(topic):
    res = get_url('https://www.zhihu.com/topic/'+topic.strip()+'/hot')
    res_soup = BeautifulSoup(res.content, 'html.parser')
    print res_soup.find('h1', 'TopicCard-titleText').text

#TODO: grab posts, at first from static page, then dynamically
#TODO: construct file structure/data schema
#TODO: grab all comments from post
