'''
Created on May 5, 2017

@author: Jicheng Wang 
'''
from bs4 import BeautifulSoup
import mechanize
import time
import urllib
import string
import os


def downloadProcess(html, base, filetype, linkList):
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        linkText = str(link.get('href'))
        
        if filetype in linkText:
            slashList = [i for i, ind in enumerate(linkText) if ind == '/']
            directoryName = linkText[(slashList[0]+1):slashList[1]]
            if not os.path.exists(directoryName):
                os.makedirs(directoryName)
                
            image = urllib.URLopener()
            linkGet = base + linkText
            filesave = string.lstrip(linkText, '/')
            image.retrieve(linkGet, filesave)
        elif "htm" in linkText:
            linkList.append(link)

start = "http://" + raw_input("where would you like to start searching\n")
filetype = raw_input("what file type are you looking for\n")

numSlash = start.count('/')
slashList = [i for i, ind in enumerate(start) if ind == '/']

if (len(slashList) >= 3):
    third = slashList[2]
    base = start[:third]
else:
    base = start


br = mechanize.Browser()
r = br.open(start)
html = r.read()
linkList = []

print "parsing" + start
downloadProcess(html, base, filetype, linkList)

for leftover in linkList:
    time.sleep(0.1)
    linkText = str(leftover.get('href'))
    print "parsing" +base + linkText
    br = mechanize.Browser()
    r = br.open(base + linkText)
    html = r.read()
    linkList = []
    downloadProcess(html, base, filetype, linkList)
    
        
    
