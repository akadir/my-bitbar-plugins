#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

username = "VENETHIS"

url = "https://twitter.com/" + username

req = urllib2.Request(url)
req.add_header('User-agent', 'Mozilla/5.0\
            (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
            Chrome/23.0.1271.97 Safari/537.11')

html_page = urllib2.urlopen(req)

if html_page.getcode() == 200:
    soup = BeautifulSoup(html_page,"html.parser")
    tweet_count = soup.find('div', attrs={'class':'statnum'})
    print tweet_count.string.rstrip("\n\r")
 #   for div in soup.find_all('div', attrs={'class':'statnum'}):
 #       print div.string
else:
    print "Error loading page"

print "---"
print username

