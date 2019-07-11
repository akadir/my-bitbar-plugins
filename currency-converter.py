#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

currId = "EURTRY=X"
currSymbolOrName = "€"

url = "https://finance.yahoo.com/quote/" + currId

req = urllib2.Request(url)
req.add_header('User-agent', 'Mozilla/5.0\
            (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
            Chrome/23.0.1271.97 Safari/537.11')

html_page = urllib2.urlopen(req)

if html_page.getcode() == 200:
    soup = BeautifulSoup(html_page,"html.parser")
    link = soup.find('span', attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    print currSymbolOrName + link.string
else:
    print "Error loading page"

print "---"
print currId

