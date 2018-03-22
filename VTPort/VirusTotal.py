import requests
import json
import urllib
import sys

def getAPIKey():
    try:
        f = open('./APIKey.txt','r')
    except IOError:
        f = open('./APIKey.txt','w+')
        APIKey = raw_input('[+] Input Virus Total API Key! ')
        f.write(APIKey)
        f.close()
        return APIKey
    APIKey = f.readline()
    f.close()
    return APIKey

def checkIP(IP):
    APIKey = getAPIKey()
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip':IP,'apikey':APIKey}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    
    Detections = []
    if response_dict['response_code'] == 1:
        domains = response_dict['resolutions']
        detections = response_dict['detected_urls']
        for detection in detections:
            Detections.append(detection['url'])
        
        return [Detections]
    else:
        return [{}]
    
