# -*- coding: cp936 -*-
from bs4 import BeautifulSoup
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def processDataOfEastMoney():
    for year in range(2005, 2014):
        for quar in range(1, 5):
            processDataOfSingleQuar(year, quar)

def processDataOfSingleQuar(year, quar):
    currentYear=2013
    currentQuar=3
    if(year>currentYear):
        return
    if(year==currentYear and quar>currentQuar):
        return
    yqPart = constructYQUrlPart(year, quar)
    urlStr='http://data.eastmoney.com/bbsj/'+yqPart +'/yjbb/ggrq/1.html'
    print urlStr
    pages=getPages(urlStr)
    for pn in range(pages):
        pageUrl="http://data.eastmoney.com/bbsj/" + yqPart + "/yjbb/ggrq/" +str(pn+1) +'.html'
        print pageUrl
        #processPage(firstPageContent)

def getPages(firstPageUrl):
    html=urllib2.urlopen(firstPageUrl)
    soup=BeautifulSoup(html)
    tag=soup.find(id='PageCont').find_all('a')[6]
    print tag
    pageStr=tag.string
    print pageStr
    return int(pageStr)

def processPage(page):
    """soup = BeautifulSoup(page)"""
    
    """TBD"""

def constructYQUrlPart(year, quar):
    quar=quar*3
    if(quar<10):
        quarStr='0'+str(quar)
    else:
        quarStr=''+str(quar)
    return str(year)+quarStr
    

if __name__=="__main__":
    processDataOfEastMoney()
