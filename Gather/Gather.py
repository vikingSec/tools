import requests
from bs4 import BeautifulSoup

def getSourceList(filename = './Sources.txt'):
    f = open(filename, 'r')
    sourcelist = [[]]
    for line in f:
        line_spl = line.split(' ')
        sourcelist.append([line_spl[1], line_spl[0]])
    f.close()
    return sourcelist

def addToSourceList(sourcetype, sourcelink, filename = './Sources.txt'):
    f = open(filename, 'a')

    f.write(sourcelink+' '+sourcetype+'\n')
    f.close()
    return sourcelink+' : '+sourcetype
