#!/usr/bin/python
#coding:utf-8


import urllib,urllib2
import re

def getHtml(url):
    data = urllib2.urlopen(url)    
    return data.read()

def htmlRe(html):
    li = re.findall(r'<img class="BDE_Image" src=(.*?) size.*?>',html)
    n = 0
    for url_pic in li:
        url_pic = url_pic.strip()
	url_pic = urllib.unquote(url_pic).encode('utf-8')
        url_pic = url_pic.split('"')[1]
        #print urllib2.urlopen(url_pic).read()
        urllib.urlretrieve(url_pic, '/root/tongbu2/tieba/123/%s.jpg'%n)
	n = n + 1
def main():
    url = 'http://tieba.baidu.com/p/5141114266'
    html = getHtml(url)
    htmlRe(html)

if __name__ == '__main__':
    main()
