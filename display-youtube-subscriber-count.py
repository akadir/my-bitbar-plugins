#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

account_name = "besiktas"

url = "https://www.youtube.com/" + account_name

req = urllib2.Request(url)
req.add_header('User-agent', 'Mozilla/5.0\
            (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
            Chrome/23.0.1271.97 Safari/537.11')

html_page = urllib2.urlopen(req)

if html_page.getcode() == 200:
    soup = BeautifulSoup(html_page,"html.parser")
    #print soup
    subscriber_count = soup.find('span', attrs={'class':['yt-subscription-button-subscriber-count-branded-horizontal', 'subscribed yt-uix-tooltip']})
    print subscriber_count.string.rstrip("\n\r")
else:
    print "Error loading page"

print "---"
print account_name

