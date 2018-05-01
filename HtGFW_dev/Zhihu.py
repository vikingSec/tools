from bs4 import BeautifulSoup
import requests
import json


def get_url(url):
    
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
<<<<<<< HEAD
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_zap=af470e5b-b255-4288-980a-e0225667b9cd; capsion_ticket="2|1:0|10:1525134921|14:capsion_ticket|44:YzhkMWY3ZDg0ZjU3NGIxMzg5NmQxYWQ2MWQ5YjAxYzY=|9ab71797a53e2df32ef135734ee4cb5125b1e5f10afb77d76d92dba4919a1843"; q_c1=d719b1057ebc45de8cfb9ff18dcf2ab3|1524862369000|1524862369000; r_cap_id="ZmUzNjBmODIwY2Q1NDc2OTlhODU3OGEzZmIyMDkwNGM=|1525129362|e003e40f5fa87b5c901d466a66ca5276f15a4a39"; cap_id="ZGQ1NzZmZGZlZmFiNDVmNjg3NWI4ODJlYWQ0MWU0YjA=|1525129362|62f8f017a5e712df23f6744d278cc10fbfb8a908"; l_cap_id="ZmYxYWQzMTM3MTgxNGUxMWI5NjkxN2JiZGRiODg3NmU=|1525129362|d528ce444c74250487efbce8c804921d4650636a"; _xsrf=17fcbd1b-6921-41d5-8cd0-c4a64831a7d4; d_c0="ALBuLxOGgg2PTtyza3wErU3la74KA7_Z86A=|1524877598"; l_n_c=1; n_c=1',
        'Host': 'www.zhihu.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'}
=======
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.5',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
<<<<<<< HEAD
                'Cookie': '_zap=af470e5b-b233-4288-980a-e0225667b9cd; capsion_ticket="2|1:0|10:1524686526|14:capsion_ticket|44:MDY4MGI3NGYzNDc3NDQ4NDljMDA3MjdlMmI0ZmYzMjY=|97d618ffbcce4f686bb4d9926c5b7113562d30c1d474349dc521ffe1de3eebef"; q_c1=d719b1057ebc45de8cfb9ff18dcf2ab3|1524862369000|1524862369000; r_cap_id="NGQzOTc2Y2Q4NTNmNDM5NThmYTEzYzc2ZDkwNjJjYjA=|1525126005|5605ceb5235ef59ff6529a7d3cf671c7dcd471ab"; cap_id="MzU4ZGY0MWYxNWZkNGRkMDgwOTMwMzBhMzQ4YzA1ZWY=|1525126005|9cd730ac2036625e8d451a3f528adf11865d559e"; l_cap_id="MDkzZmQ0NjZmNTNmNGU2YjgwNWJkNjBjMDY4YTMwNmQ=|1525126005|ead609b0c4b5c0b918552f626aaa8e949a43aae1"; _xsrf=17fcbd1b-6921-41d5-8cd0-c4a64831a7d4; d_c0="ALBuLxOGgg2PTtyza3wErU3la74KA7_Z86A=|1524877598"; l_n_c=1; n_c=1',
=======
                'Cookie': '_zap=af470e5b-b255-4288-980a-e0225667b9cd; capsion_ticket="2|1:0|10:1525133511|14:capsion_ticket|44:ZjdlMDJiMTdlMDk0NDI3MzhiNjNmM2YzZDNkMWUwZGY=|202e74e5b2c604d914bc8e598a191250a1d72ae3efaf5ca5897b56df4e09ffba"; q_c1=d719b1057ebc45de8cfb9ff18dcf2ab3|1524862369000|1524862369000; r_cap_id="ZmUzNjBmODIwY2Q1NDc2OTlhODU3OGEzZmIyMDkwNGM=|1525129362|e003e40f5fa87b5c901d466a66ca5276f15a4a39"; cap_id="ZGQ1NzZmZGZlZmFiNDVmNjg3NWI4ODJlYWQ0MWU0YjA=|1525129362|62f8f017a5e712df23f6744d278cc10fbfb8a908"; l_cap_id="ZmYxYWQzMTM3MTgxNGUxMWI5NjkxN2JiZGRiODg3NmU=|1525129362|d528ce444c74250487efbce8c804921d4650636a"; _xsrf=17fcbd1b-6921-41d5-8cd0-c4a64831a7d4; d_c0="ALBuLxOGgg2PTtyza3wErU3la74KA7_Z86A=|1524877598"; l_n_c=1; n_c=1',
>>>>>>> c6bf35e4c7963087c704de3f08b4acafb1eb01a4
                'Host': 'zhihu.com',
                'Referer': 'https://www.zhihu.com/topic/19558642/hot',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'}
>>>>>>> 844f26459479c77268e5a9db79779ba19cf987fd
    cookies = {'_xsrf':'d2016f2f-9cb8-46d7-b60e-e358e4ae3378',
               '_zap':'17fcbd1b-6921-41d5-8cd0-c4a64831a7d4',
               'capsion_ticket':'"2|1:0|10:1521441001|14:capsion_ticket|44:ODY0ODIwNDY3MTZjNDQ2ZWEzMzY0MTUyYmUzYmIyY2Y=|8999178ca9eca48ff5a58634ff875758f0c652faf570b4cdfff44b58b7ee1451"',
               'd_c0':'"AHDv1_VWhg2PTm1obeocD_UW3AwNYNUA7m0=|1525133683"',
               'q_c1':'a425ea5549a447938faa642092051460|1521440815000|1516935035000',
               'unlock_ticket':'"AADALBf8cQomAAAAYAJVTWpgr1qJugy4PDM7_uLRXnEshPuWB12czg=="',
               'z_c0':'"2|1:0|10:1521441122|4:z_c0|92:Mi4xMGxGbEF3QUFBQUFBc0t1c3lVOVBEU1lBQUFCZ0FsVk5ZcWVjV3dEclpxYVVzcW5oN2RsUmJfejJuaVFfTGViN0hR|146622b2b39772b7212ae40b7b59217bcccca30163f184628ef96ed9744cf452"'}

    return requests.get(url, headers=headers, cookies=cookies)

def get_url_zl(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.5',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie':'_zap=af470e5b-b255-4288-980a-e0225667b9cd; capsion_ticket="2|1:0|10:1525134921|14:capsion_ticket|44:YzhkMWY3ZDg0ZjU3NGIxMzg5NmQxYWQ2MWQ5YjAxYzY=|9ab71797a53e2df32ef135734ee4cb5125b1e5f10afb77d76d92dba4919a1843"; q_c1=d719b1057ebc45de8cfb9ff18dcf2ab3|1524862369000|1524862369000; r_cap_id="ZmUzNjBmODIwY2Q1NDc2OTlhODU3OGEzZmIyMDkwNGM=|1525129362|e003e40f5fa87b5c901d466a66ca5276f15a4a39"; cap_id="ZGQ1NzZmZGZlZmFiNDVmNjg3NWI4ODJlYWQ0MWU0YjA=|1525129362|62f8f017a5e712df23f6744d278cc10fbfb8a908"; l_cap_id="ZmYxYWQzMTM3MTgxNGUxMWI5NjkxN2JiZGRiODg3NmU=|1525129362|d528ce444c74250487efbce8c804921d4650636a"; _xsrf=17fcbd1b-6921-41d5-8cd0-c4a64831a7d4; d_c0="ALBuLxOGgg2PTtyza3wErU3la74KA7_Z86A=|1524877598"; l_n_c=1; n_c=1',
'Host': 'zhuanlan.zhihu.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'}
    cookies = {'_xsrf':'17fcbd1b-6921-41d5-8cd0-c4a64831a7d4',
               '_zap':'af470e5b-b255-4288-980a-e0225667b9cd',
               'capsion_ticket':'"2|1:0|10:1525133511|14:capsion_ticket|44:ZjdlMDJiMTdlMDk0NDI3MzhiNjNmM2YzZDNkMWUwZGY=|202e74e5b2c604d914bc8e598a191250a1d72ae3efaf5ca5897b56df4e09ffba"',
               'd_c0':'"ALBuLxOGgg2PTtyza3wErU3la74KA7_Z86A=|1524877598"',
               'q_c1':'d719b1057ebc45de8cfb9ff18dcf2ab3|1524862369000|1524862369000',
               'unlock_ticket':'"AADALBf8cQomAAAAYAJVTWpgr1qJugy4PDM7_uLRXnEshPuWB12czg=="',
               'z_c0':'"2|1:0|10:1521441122|4:z_c0|92:Mi4xMGxGbEF3QUFBQUFBc0t1c3lVOVBEU1lBQUFCZ0FsVk5ZcWVjV3dEclpxYVVzcW5oN2RsUmJfejJuaVFfTGViN0hR|146622b2b39772b7212ae40b7b59217bcccca30163f184628ef96ed9744cf452"'}

    return requests.get(url, headers=headers, cookies=cookies)
    

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

def getPostBody(postID, posttype = 'question'):
    if posttype == 'question':
        res = get_url('https://www.zhihu.com/question/'+postID)
        soup = BeautifulSoup(res.content, 'html.parser')
        question_body = soup.find('span', 'RichText', {'data-reactid':'97'}).text
        print(question_body)


def getPostTitle(postID, posttype = 'question'):
    if posttype == 'question':
        res = get_url('https://www.zhihu.com/question/'+postID)
        soup = BeautifulSoup(res.content, 'html.parser')
        question_title = soup.find('h1', 'QuestionHeader-title').text
        print(question_title)

def dumpTopic(topicID, number = 20):
    ret = ""
    ret+=dumpTopic_hot(topicID, number)
    ret+=dumpTopic_unanswered(topicID, number)
    return ret
    


def dumpTopic_hot(topicID, number = 20):
    topicURL = 'https://www.zhihu.com/topic/'+str(topicID).strip()+'/hot'
    res = get_url(topicURL)

    soup = BeautifulSoup(res.content, 'html.parser')
    question_list = soup.find_all('div','List-item TopicFeedItem')

    ret = ""
    
    
    
    for item in list(question_list):
        art_item = item.find('div', {'class':'ContentItem ArticleItem'})
        ans_item = item.find('div', {'class':'ContentItem AnswerItem'})
        if(art_item):
            
            url = item.find('a', {'data-za-detail-view-element_name':'Title'})['href']
            url = url.replace('//','https://')
            art_res = get_url_zl(url)
            soup = BeautifulSoup(art_res.content, 'html.parser')

            

            posttype = 'article'
            postid = json.loads(soup.find('div', {'class':'Post-content'})['data-zop'])['itemId']
            author = json.loads(soup.find('div', {'class':'Post-content'})['data-zop'])['authorName']
            title = json.loads(soup.find('div', {'class':'Post-content'})['data-zop'])['title']
            art_content = soup.find('div',{'class':'RichText Post-RichText'}).text
            #print('?Topic ID: '+topicID+'\n'+'Post ID: '+str(postid)+'\n'+'URL: '+url+'\n'+'Author: '+author+'\n'+'Post Type:'+posttype+'\n'+'Title: '+title+'\n\n')
            ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author.strip()+'\n'+title.strip()+'\n'+art_content.strip()+'\n\n:\n')

        if(ans_item):
            url = item.find('a', {'data-za-detail-view-element_name':'Title'})['href']
            url = 'https://www.zhihu.com'+url
            ans_res = get_url(url)
            soup = BeautifulSoup(ans_res.content, 'html.parser')

            
            posttype = 'answer'
            postid = json.loads(soup.find('div',{'class':'ContentItem AnswerItem'})['data-zop'])['itemId']
            author = json.loads(soup.find('div',{'class':'ContentItem AnswerItem'})['data-zop'])['authorName']
            question_title = soup.find('div',{'class':'QuestionPage'}).find('meta', {'itemprop':'name'})['content']
            ans_content = soup.find('span',{'class':'RichText CopyrightRichText-richText'}).text
            
            ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url.strip()+'\n'+author.strip()+'\n'+question_title.strip()+'\n'+ans_content.strip()+'\n\n:\n')
            question_url = soup.find('meta',{'itemprop':'url'})['content']
            ques_res = get_url(question_url)
            soup = BeautifulSoup(ques_res.content, 'html.parser')

            posttype = 'question'
            postid = question_url.split('/')[4]
            
            title = soup.find('h1', {'class':'QuestionHeader-title'}).text
            content = soup.find('span', {'class':'RichText','itemprop':'text'}).text
            
            ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+question_url.strip()+'\n'+'UNKNOWN'+'\n'+title.strip()+'\n'+content.strip()+'\n\n:\n')

    return ret

def dumpTopic_unanswered(topicID, number = 20):
    topicURL = 'https://www.zhihu.com/topic/'+str(topicID).strip()+'/unanswered'
    res = get_url(topicURL)

    soup = BeautifulSoup(res.content, 'html.parser')
    question_list = soup.find_all('div','List-item TopicFeedItem')

    ret = ""
    
    
    
    for item in list(question_list):
        art_item = item.find('div', {'class':'ContentItem ArticleItem'})
        ans_item = item.find('div', {'class':'ContentItem AnswerItem'})
        if(art_item):
            
            url = item.find('a', {'data-za-detail-view-element_name':'Title'})['href']
            url = url.replace('//','https://')
            art_res = get_url_zl(url)
            soup = BeautifulSoup(art_res.content, 'html.parser')

            

            posttype = 'article'
            postid = json.loads(soup.find('div', {'class':'Post-content'})['data-zop'])['itemId']
            author = json.loads(soup.find('div', {'class':'Post-content'})['data-zop'])['authorName']
            title = json.loads(soup.find('div', {'class':'Post-content'})['data-zop'])['title']
            art_content = soup.find('div',{'class':'RichText Post-RichText'}).text
            #print('?Topic ID: '+topicID+'\n'+'Post ID: '+str(postid)+'\n'+'URL: '+url+'\n'+'Author: '+author+'\n'+'Post Type:'+posttype+'\n'+'Title: '+title+'\n\n')
            ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url+'\n'+author.strip()+'\n'+title.strip()+'\n'+art_content.strip()+'\n\n:\n')

        if(ans_item):
            url = item.find('a', {'data-za-detail-view-element_name':'Title'})['href']
            url = 'https://www.zhihu.com'+url
            ans_res = get_url(url)
            soup = BeautifulSoup(ans_res.content, 'html.parser')

            
            posttype = 'answer'
            postid = json.loads(soup.find('div',{'class':'ContentItem AnswerItem'})['data-zop'])['itemId']
            author = json.loads(soup.find('div',{'class':'ContentItem AnswerItem'})['data-zop'])['authorName']
            question_title = soup.find('div',{'class':'QuestionPage'}).find('meta', {'itemprop':'name'})['content']
            ans_content = soup.find('span',{'class':'RichText CopyrightRichText-richText'}).text
            
            ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+url.strip()+'\n'+author.strip()+'\n'+question_title.strip()+'\n'+ans_content.strip()+'\n\n:\n')
            question_url = soup.find('meta',{'itemprop':'url'})['content']
            ques_res = get_url(question_url)
            soup = BeautifulSoup(ques_res.content, 'html.parser')

            posttype = 'question'
            postid = question_url.split('/')[4]
            
            title = soup.find('h1', {'class':'QuestionHeader-title'}).text
            content = soup.find('span', {'class':'RichText','itemprop':'text'}).text
            
            ret+=(topicID+'\n'+posttype+'\n'+str(postid)+'\n'+question_url.strip()+'\n'+'UNKNOWN'+'\n'+title.strip()+'\n'+content.strip()+'\n\n:\n')

    return ret


