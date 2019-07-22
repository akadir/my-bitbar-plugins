#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys
from bs4 import BeautifulSoup
from collections import OrderedDict

def get_curr_price(symbol, currency_id):
    url = "https://finance.yahoo.com/quote/"+currency_id

    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0\
                (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
                Chrome/23.0.1271.97 Safari/537.11')

    html_page = urllib2.urlopen(req)

    if html_page.getcode() == 200:
        soup = BeautifulSoup(html_page,"html.parser")
        link = soup.find('span', attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        print symbol + str(round(float(link.string),2))
    else:
        print "Error loading page"


reload(sys)
sys.setdefaultencoding('utf8')

currencies = OrderedDict()
currencies['$'] = 'TRY=X'
currencies['€'] = 'EURTRY=X'

for key, value in currencies.items():
    get_curr_price(key, value)
    print "---"


