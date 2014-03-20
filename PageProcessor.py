from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visualstock.settings")
from djangoapp.frecord import FinanceRecord
import urllib2

import sys 
reload(sys)
sys.setdefaultencoding('utf8') 



def processPage(curQuar, pageUrl):
    html=urllib2.urlopen(pageUrl)
    soup=BeautifulSoup(html)
    columnLen=soup.find_all('table')[0].thead.find_all('tr')[0].length
    for tag in soup.find_all('table')[0].tbody.find_all('tr'):
        tdlist = tag.find_all('td')
        if(columnLen==13):
            issuedatestr=tdlist[16].string
        else:
            issuedatestr=tdlist[15].string
        fRecord = FinanceRecord(stock_no=tdlist[1].string,
                                  quarter=curQuar,
                                  stock_name=tdlist[2].string,
                                  link='',
                                  eps=strToDecimal(tdlist[4].string),
                                  revenue=strToDecimal(tdlist[5].string),
                                  revenue_growth_byyear=strToDecimal(tdlist[6].string),
                                  revenue_growth_byquar=strToDecimal(tdlist[7].string),
                                  earning=strToDecimal(tdlist[8].string),
                                  earning_growth_byyear=strToDecimal(tdlist[9].string),
                                  earning_growth_byquar=strToDecimal(tdlist[10].string),
                                  net_assets=strToDecimal(tdlist[11].string),
                                  roe=strToDecimal(tdlist[12].string),
                                  cash_flow_pershare=strToDecimal(tdlist[13].string),
                                  margin=strToDecimal(tdlist[14].string),
                                  issuedate='-'.join([curQuar[0:4], issuedatestr]))
        try:
            fRecord.save()
        except Exception, e:
            print e
            fRecord = FinanceRecord(stock_no=tdlist[1].string,
                                      quarter=curQuar,
                                      stock_name=tdlist[2].string,
                                      link='',
                                      eps=None,
                                      revenue=None,
                                      revenue_growth_byyear=None,
                                      revenue_growth_byquar=None,
                                      earning=None,
                                      earning_growth_byyear=None,
                                      earning_growth_byquar=None,
                                      net_assets=None,
                                      roe=None,
                                      cash_flow_pershare=None,
                                      margin=None,
                                      issuedate=None)
            fRecord.save()
            
        

def strToDecimal(strval):
    if cmp(strval, '-')==0:
        return None
    else:
        return strval

if __name__=="__main__":
    processPage("201306", "http://data.eastmoney.com/bbsj/201306/yjbb.html")
                                  
